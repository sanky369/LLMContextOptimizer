git clone [repository-url]
cd llm-context-optimizer
```

2. Install dependencies:
```bash
pip install flask flask-wtf wtforms
```

## Usage

### Web Interface

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:3000`

3. Use the web interface to:
   - Input text for optimization
   - Select optimization options
   - View and copy results
   - Access detailed documentation

### CLI Usage

Process text directly:
```bash
python cli.py "Your text here" --structure json
```

Process from file:
```bash
python cli.py input.txt --output result.json --structure json
```

CLI options:
- `--no-compression`: Disable text compression
- `--no-abbreviations`: Disable abbreviations
- `--base64`: Enable base64 encoding
- `--structure`: Choose output format (json/xml)
- `--no-token-optimization`: Disable token optimization
- `--output`: Specify output file

### API Integration

The LLM Context Optimizer provides a RESTful API for integration with other applications. For detailed API documentation, please see [API Documentation](docs/api.md).

Quick start example:
```bash
curl -X POST http://localhost:3000/api/optimize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The natural language processing model uses deep learning techniques.",
    "use_compression": true,
    "use_abbreviations": true,
    "structure_format": "json"
  }'