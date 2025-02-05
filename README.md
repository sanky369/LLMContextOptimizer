git clone [repository-url]
cd llm-context-optimizer
```

2. Install dependencies:
```bash
pip install flask flask-wtf
```

## Usage

### Web Interface

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:3000`

### CLI

Process text directly:
```bash
python cli.py "Your text here" --structure json
```

Process from file:
```bash
python cli.py input.txt --output result.json --structure json
```

## API Documentation

### REST API Endpoint

- **URL**: `/api/optimize`
- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Body Options:

```json
{
  "text": "Your text to optimize",
  "use_compression": true,
  "use_abbreviations": true,
  "use_base64": false,
  "structure_format": "json",
  "optimize_tokens": true,
  "minify_code": false,
  "use_pseudo_urls": false
}
```

All options are optional except `text`. Default values shown above.

#### Response Format:

```json
{
  "original": "Original text",
  "compressed": "Compressed version",
  "abbreviated": {
    "text": "Abbreviated text",
    "definitions": {
      "original phrase": "abbreviation"
    }
  },
  "minified_code": "Minified version of code blocks",
  "with_references": "Text with pseudo-URL references",
  "token_optimized": "Token optimized text",
  "structured": "{...}",
  "base64": "Base64 encoded text",
  "semantic_hash": "CTX_123"
}
```

#### Example cURL Request:

```bash
curl -X POST http://localhost:3000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The natural language processing model uses deep learning techniques.",
    "use_compression": true,
    "use_abbreviations": true,
    "structure_format": "json"
  }'
```

#### Example Response:

```json
{
  "original": "The natural language processing model uses deep learning techniques.",
  "compressed": "natural language processing model uses deep learning techniques",
  "abbreviated": {
    "text": "NLP model uses DL techniques",
    "definitions": {
      "natural language processing": "NLP",
      "deep learning": "DL"
    }
  },
  "structured": {
    "ctx": {
      "topic": "context_optimization",
      "keywords": ["NLP", "model", "uses", "DL", "techniques"],
      "content": "NLP model uses DL techniques"
    }
  },
  "semantic_hash": "CTX_789"
}