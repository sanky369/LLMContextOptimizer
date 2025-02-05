import argparse
import sys
import json
from llm_context_optimizer import LLMContextOptimizer

def main():
    parser = argparse.ArgumentParser(description='LLM Context Optimizer CLI')
    parser.add_argument('input', help='Input text or file path (use - for stdin)')
    parser.add_argument('--no-compression', action='store_true', help='Disable text compression')
    parser.add_argument('--no-abbreviations', action='store_true', help='Disable abbreviations')
    parser.add_argument('--base64', action='store_true', help='Enable base64 encoding')
    parser.add_argument('--structure', choices=['json', 'xml'], help='Output structure format')
    parser.add_argument('--no-token-optimization', action='store_true', help='Disable token optimization')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    # Read input
    if args.input == '-':
        text = sys.stdin.read()
    else:
        try:
            with open(args.input, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            text = args.input
    
    # Initialize optimizer
    optimizer = LLMContextOptimizer()
    
    # Process text
    result = optimizer.optimize(
        text=text,
        use_compression=not args.no_compression,
        use_abbreviations=not args.no_abbreviations,
        use_base64=args.base64,
        structure_format=args.structure,
        optimize_tokens=not args.no_token_optimization
    )
    
    # Format output
    output = json.dumps(result, indent=2)
    
    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)

if __name__ == '__main__':
    main()
