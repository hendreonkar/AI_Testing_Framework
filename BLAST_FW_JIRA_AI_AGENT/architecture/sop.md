# Architecture SOP

## Objective
Build a lightweight React application that:
- accepts JIRA and OpenRouter settings
- fetches a JIRA issue by ID (e.g. QT-2)
- generates a QA test plan with sections: Scope, Test Cases, Risks
- supports output display in UI, Markdown export, file save, and clipboard copy

## Inputs
- Jira credentials: email, token, base URL
- OpenAI API key and model
- GROQ/OpenAI API endpoint details
- Jira issue ID

## Output
- Structured test plan data
- Rendered UI text
- Markdown export
- Optional file save / clipboard copy

## Rules
- Use JIRA REST API as single source of truth for issue data
- Do not invent Jira issue details
- Keep output concise and structured
- Include required sections explicitly
