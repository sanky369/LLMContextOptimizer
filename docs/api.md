# LLM Context Optimizer API Documentation

This document provides detailed information about the LLM Context Optimizer REST API endpoints.

## Base URL

```
http://your-domain:3000/api
```

## Endpoints

### Optimize Text

Optimizes and processes text using various strategies for efficient LLM context delivery.

- **URL**: `/optimize`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| text | string | Yes | - | The input text to optimize |
| use_compression | boolean | No | true | Enable text compression |
| use_abbreviations | boolean | No | true | Enable abbreviation replacement |
| use_base64 | boolean | No | false | Enable base64 encoding |
| structure_format | string | No | null | Output structure format ('json' or 'xml') |
| optimize_tokens | boolean | No | true | Enable token optimization |
| minify_code | boolean | No | false | Enable code minification |
| use_pseudo_urls | boolean | No | false | Enable pseudo-URL references |

### Response Format

The response is a JSON object containing various optimized versions of the input text.

```json
{
  "original": "Original input text",
  "compressed": "Compressed version of text",
  "abbreviated": {
    "text": "Abbreviated version",
    "definitions": {
      "original phrase": "abbreviation"
    }
  },
  "minified_code": "Minified version of code blocks",
  "with_references": "Text with pseudo-URL references",
  "token_optimized": "Token-optimized version",
  "structured": "{...}",
  "base64": "Base64 encoded version",
  "semantic_hash": "CTX_123"
}
```

### Example Use Cases

#### 1. Basic Text Optimization

```bash
curl -X POST http://localhost:3000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The natural language processing model uses deep learning techniques."
  }'
```

#### 2. Code Minification

```bash
curl -X POST http://localhost:3000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "def calculate_average(numbers):\n    total = sum(numbers)\n    return total / len(numbers)",
    "minify_code": true
  }'
```

#### 3. Structured Output with Abbreviations

```bash
curl -X POST http://localhost:3000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The machine learning model uses deep learning and natural language processing.",
    "use_abbreviations": true,
    "structure_format": "json"
  }'
```

### Error Handling

The API uses standard HTTP status codes for error responses:

- `200 OK`: Request successful
- `400 Bad Request`: Invalid input or parameters
- `413 Payload Too Large`: Input text exceeds 16MB limit
- `500 Internal Server Error`: Server-side error

Error Response Format:
```json
{
  "error": "Error message describing what went wrong"
}
```

### Rate Limiting

- Maximum request size: 16MB
- Rate limit: None currently implemented

### Best Practices

1. **Input Size**
   - Keep input text under 16MB
   - Split large texts into smaller chunks if needed

2. **Optimization Selection**
   - Enable only needed optimization features
   - Use compression and abbreviations for long texts
   - Use minify_code only for code-heavy content

3. **Error Handling**
   - Always check response status codes
   - Implement proper error handling in your client code

### Status Codes Reference

| Status Code | Description |
|------------|-------------|
| 200 | Successful optimization |
| 400 | Invalid parameters or input |
| 413 | Request too large |
| 500 | Server error |

## SDK Examples

### Python

```python
import requests
import json

def optimize_text(text, **options):
    url = "http://localhost:3000/api/optimize"
    payload = {
        "text": text,
        **options
    }
    response = requests.post(url, json=payload)
    return response.json()

# Example usage
result = optimize_text(
    "The natural language processing model uses deep learning.",
    use_abbreviations=True,
    structure_format="json"
)
print(json.dumps(result, indent=2))
```

### JavaScript

```javascript
async function optimizeText(text, options = {}) {
  const response = await fetch('http://localhost:3000/api/optimize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text,
      ...options,
    }),
  });
  return response.json();
}

// Example usage
optimizeText(
  'The natural language processing model uses deep learning.',
  { useAbbreviations: true, structureFormat: 'json' }
).then(console.log);
```
