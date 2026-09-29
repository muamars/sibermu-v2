const DEFAULT_WEBHOOK_URL = 'https://dlh-n8n.nurarif.in/webhook/sibermu'
const MAX_BODY_BYTES = 16 * 1024

async function readJsonBody(request) {
  const chunks = []
  let size = 0

  for await (const chunk of request) {
    size += chunk.length
    if (size > MAX_BODY_BYTES) {
      const error = new Error('Request body terlalu besar')
      error.status = 413
      throw error
    }
    chunks.push(chunk)
  }

  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'))
  } catch {
    const error = new Error('Request body harus berupa JSON yang valid')
    error.status = 400
    throw error
  }
}

export async function chatController(request, response) {
  try {
    if (!request.headers['content-type']?.includes('application/json')) {
      response.writeHead(415, { 'Content-Type': 'application/json; charset=utf-8' })
      response.end(JSON.stringify({ message: 'Content-Type harus application/json' }))
      return
    }

    const { message, sessionId } = await readJsonBody(request)
    if (typeof message !== 'string' || !message.trim() || typeof sessionId !== 'string' || !sessionId.trim()) {
      response.writeHead(400, { 'Content-Type': 'application/json; charset=utf-8' })
      response.end(JSON.stringify({ message: 'message dan sessionId wajib diisi' }))
      return
    }

    const webhookUrl = process.env.CHAT_WEBHOOK_URL || DEFAULT_WEBHOOK_URL
    const upstream = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message.trim(), sessionId: sessionId.trim() }),
      signal: AbortSignal.timeout(30_000),
    })
    const body = await upstream.text()

    response.writeHead(upstream.status, {
      'Content-Type': upstream.headers.get('content-type') || 'text/plain; charset=utf-8',
      'Cache-Control': 'no-store',
    })
    response.end(body)
  } catch (error) {
    const status = error.status || (error.name === 'TimeoutError' ? 504 : 502)
    response.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8' })
    response.end(JSON.stringify({ message: status === 504 ? 'Webhook timeout' : error.message || 'Webhook tidak dapat dihubungi' }))
  }
}
