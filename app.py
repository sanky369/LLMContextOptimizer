from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired
from llm_context_optimizer import LLMContextOptimizer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # For CSRF protection

class OptimizationForm(FlaskForm):
    text = TextAreaField('Input Text', validators=[DataRequired()])
    use_compression = BooleanField('Use Compression', default=True)
    use_abbreviations = BooleanField('Use Abbreviations', default=True)
    use_base64 = BooleanField('Use Base64 Encoding', default=False)
    structure_format = SelectField('Structure Format', 
                                 choices=[('none', 'None'), 
                                        ('json', 'JSON'), 
                                        ('xml', 'XML')],
                                 default='none')
    optimize_tokens = BooleanField('Optimize Tokens', default=True)
    submit = SubmitField('Optimize')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = OptimizationForm()
    result = None
    
    if form.validate_on_submit():
        optimizer = LLMContextOptimizer()
        structure_format = form.structure_format.data
        if structure_format == 'none':
            structure_format = None
            
        result = optimizer.optimize(
            text=form.text.data,
            use_compression=form.use_compression.data,
            use_abbreviations=form.use_abbreviations.data,
            use_base64=form.use_base64.data,
            structure_format=structure_format,
            optimize_tokens=form.optimize_tokens.data
        )
        
    return render_template('index.html', form=form, result=result)

@app.route('/api/optimize', methods=['POST'])
def api_optimize():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
        
    optimizer = LLMContextOptimizer()
    result = optimizer.optimize(**data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
