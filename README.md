# Resume Optimizer Agent 🚀

An AI-powered tool that automatically tailors your resume to match job descriptions using Claude AI. This agent analyzes job postings, extracts key requirements, and optimizes your resume to maximize your chances of getting noticed.

## Features

- 📝 **Smart Resume Optimization**: Automatically reorders and emphasizes relevant experience
- 🔍 **Job Description Analysis**: Extracts key skills, requirements, and keywords
- 📊 **Match Score Calculation**: See how well your resume matches the job (0-100 score)
- 💡 **Actionable Suggestions**: Get specific recommendations for improvement
- ✅ **Truthfulness Guaranteed**: Never adds false information or fake skills
- 🎯 **Keyword Optimization**: Naturally incorporates relevant keywords from job descriptions

## Prerequisites

- Python 3.7+
- Anthropic API key ([Get one here](https://console.anthropic.com/))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/resume-optimizer.git
cd resume-optimizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or create a `.env` file:
```bash
echo "ANTHROPIC_API_KEY=your-api-key-here" > .env
```

## Usage

### Basic Resume Optimization

```bash
python resume_optimizer.py \
  --resume my_resume.txt \
  --job-description job_posting.txt \
  --output optimized_resume.txt
```

### Get Match Score Only

```bash
python resume_optimizer.py \
  --resume my_resume.txt \
  --job-description job_posting.txt \
  --score
```

### Get Suggestions Without Optimizing

```bash
python resume_optimizer.py \
  --resume my_resume.txt \
  --job-description job_posting.txt \
  --suggestions-only
```

### Combined: Score + Optimize

```bash
python resume_optimizer.py \
  --resume my_resume.txt \
  --job-description job_posting.txt \
  --output optimized_resume.txt \
  --score
```

## Python API Usage

```python
from resume_optimizer import ResumeOptimizer

# Initialize the optimizer
optimizer = ResumeOptimizer(api_key="your-api-key")

# Read your files
with open('resume.txt') as f:
    resume = f.read()
with open('job_description.txt') as f:
    job_desc = f.read()

# Get match score
score = optimizer.calculate_match_score(resume, job_desc)
print(f"Match Score: {score['overall_score']}/100")

# Get optimization suggestions
suggestions = optimizer.suggest_improvements(resume, job_desc)
for suggestion in suggestions:
    print(suggestion)

# Generate optimized resume
optimized = optimizer.optimize_resume(resume, job_desc)
with open('optimized_resume.txt', 'w') as f:
    f.write(optimized)
```

## How It Works

1. **Analysis Phase**: The agent analyzes the job description to extract:
   - Required skills (technical and soft skills)
   - Key responsibilities
   - Important keywords
   - Experience level requirements
   - Industry-specific terminology

2. **Optimization Phase**: Your resume is optimized by:
   - Reordering experiences to highlight relevant ones
   - Incorporating job-specific keywords naturally
   - Emphasizing matching skills
   - Tailoring the summary/objective
   - Quantifying achievements where possible

3. **Scoring Phase**: The match is evaluated on:
   - Overall compatibility (0-100)
   - Keyword coverage
   - Skills alignment
   - Experience relevance

## File Formats Supported

- Plain text (`.txt`)
- Markdown (`.md`)
- Any text-based format

For best results, use well-structured text resumes with clear sections.

## Best Practices

1. **Start with a strong base resume**: Include all your real experiences and skills
2. **Be specific**: The more detailed your job description input, the better the optimization
3. **Review the output**: Always review and personalize the optimized version
4. **Maintain truthfulness**: The tool won't add fake skills, but you should verify all content
5. **Use for multiple applications**: Optimize your resume for each job you apply to

## Privacy & Security

- Your resume data is sent to Anthropic's API for processing
- No data is stored by this tool (only passed to Claude API)
- Keep your API key secure and never commit it to version control
- Review Anthropic's [privacy policy](https://www.anthropic.com/privacy)

## Limitations

- Requires an active internet connection
- API usage incurs costs (see [Anthropic pricing](https://www.anthropic.com/pricing))
- Works best with text-based resumes (not PDFs with complex formatting)
- Output quality depends on the quality of input resume and job description

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Disclaimer

This tool is designed to help optimize your resume presentation, not to fabricate qualifications. Always ensure your resume accurately represents your skills and experience. The tool's suggestions should be reviewed and customized before use.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Note**: This tool uses Claude AI by Anthropic. Make sure you have a valid API key and understand the associated costs before using it extensively.
