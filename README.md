# LLM Context Optimizer

A Python-based utility for optimizing and compressing context delivery to Large Language Models (LLMs), featuring advanced text processing capabilities and a web interface.

## Features

- **Multiple Optimization Strategies**:
  - Text compression and redundancy removal
  - Token optimization for efficient LLM processing
  - Abbreviation handling with definition mapping
  - Code minification for embedded code blocks
  - Pseudo-URL references for technical concepts
  - Base64 encoding support
  - Structured output formats (JSON/XML)

- **Web Interface**:
  - User-friendly UI for text optimization
  - Real-time size tracking
  - Multiple optimization options
  - Copy-to-clipboard functionality
  - Detailed help documentation

- **CLI Support**:
  - Command-line interface for batch processing
  - Support for file input/output
  - Multiple output format options

## Installation

1. Clone the repository:
```bash
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

## API Reference

### REST API

Endpoint: `/api/optimize`
Method: `POST`
Content-Type: `application/json`

Request body:
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

Response:
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
  "token_optimized": "Token optimized text",
  "structured": "{...}",
  "semantic_hash": "CTX_123"
}
```

## Configuration

- Maximum input size: 16MB
- Supported output formats: JSON, XML
- Server host: 0.0.0.0
- Default port: 3000

## Development

- Python 3.x
- Flask for web interface
- Regular expressions for text processing
- Modular architecture for easy extension

## License

MIT License (See LICENSE file for details)
