# Quick Start Guide

## Setup (5 minutes)

1. **Get your Anthropic API Key**
   - Visit: https://console.anthropic.com/
   - Sign up or log in
   - Go to API Keys section
   - Create a new key and copy it

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Your API Key**
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```

## Quick Test with Examples

Try the tool with the provided sample files:

```bash
# Get match score
python resume_optimizer.py \
  --resume examples/sample_resume.txt \
  --job-description examples/sample_job_description.txt \
  --score

# Get suggestions
python resume_optimizer.py \
  --resume examples/sample_resume.txt \
  --job-description examples/sample_job_description.txt \
  --suggestions-only

# Generate optimized resume
python resume_optimizer.py \
  --resume examples/sample_resume.txt \
  --job-description examples/sample_job_description.txt \
  --output my_optimized_resume.txt
```

## Use With Your Own Resume

1. Save your resume as a `.txt` file (plain text works best)
2. Save the job description as a `.txt` file
3. Run the optimizer:

```bash
python resume_optimizer.py \
  --resume your_resume.txt \
  --job-description job_posting.txt \
  --output optimized_resume.txt \
  --score
```

## Tips for Best Results

- **Resume Format**: Use clear section headers (Summary, Experience, Skills, Education)
- **Job Description**: Include the full job posting, not just a link
- **Review Output**: Always review and personalize the optimized version
- **Iterate**: Try different phrasings in your base resume to see what works best

## Cost Estimation

- Each optimization uses approximately 5,000-10,000 tokens
- At current Claude pricing, this costs roughly $0.01-0.03 per optimization
- Suggestions-only and scoring use fewer tokens

## Troubleshooting

**"ANTHROPIC_API_KEY not found"**
- Make sure you've exported the environment variable
- Or create a `.env` file with your key

**"Module not found"**
- Run `pip install -r requirements.txt`

**"Invalid API key"**
- Check that you copied the full key from the Anthropic console
- Make sure there are no extra spaces

## Next Steps

- Customize the agent in `resume_optimizer.py` for your specific needs
- Add support for different file formats (docx, PDF)
- Create a web interface
- Integrate with job board APIs

Happy job hunting! 🚀
