# gemini.md

## Data Schema

### Input
- jiraId: string
- jiraEmail: string
- jiraToken: string
- jiraBaseUrl: string
- openRouterKey: string
- openRouterModel: string
- openRouterApiUrl: string
- settings: object
  - outputFormats: string[] # e.g. ["ui", "markdown", "file", "clipboard"]

Example input:
```json
{
  "jiraId": "QT-2",
  "jiraEmail": "user@example.com",
  "jiraToken": "<jira-token>",
  "jiraBaseUrl": "https://yourcompany.atlassian.net",
  "openRouterKey": "<openrouter-key>",
  "openRouterModel": "z-ai/glm-5.2",
  "openRouterApiUrl": "https://openrouter.ai/api/v1/chat/completions",
  "settings": {
    "outputFormats": ["ui", "markdown", "file", "clipboard"]
  }
}
```

### Output
- jiraIssue: object
  - key: string
  - summary: string
  - description: string
  - type: string
  - priority: string
  - labels: string[]
  - status: string
  - url: string
- testPlan: object
  - scope: string
  - testCases: array<object>
    - title: string
    - description: string
    - steps: string[]
    - expectedResult: string
    - priority: string
  - risks: string[]
  - notes: string
- outputMetadata: object
  - generatedAt: string
  - source: string

Example output:
```json
{
  "jiraIssue": {
    "key": "QT-2",
    "summary": "Sample issue summary",
    "description": "Detailed issue description...",
    "type": "Story",
    "priority": "Medium",
    "labels": ["ui", "regression"],
    "status": "To Do",
    "url": "https://yourcompany.atlassian.net/browse/QT-2"
  },
  "testPlan": {
    "scope": "Test coverage for the QT-2 requirement.",
    "testCases": [
      {
        "title": "Verify login flow",
        "description": "Ensure the user can log in successfully.",
        "steps": ["Open login page", "Enter credentials", "Submit form"],
        "expectedResult": "User is authenticated and redirected to dashboard.",
        "priority": "High"
      }
    ],
    "risks": ["Incomplete Jira description", "Flaky authentication service"],
    "notes": "Generated from Jira issue QT-2 using GROQ/OpenAI.",
  },
  "outputMetadata": {
    "generatedAt": "2026-06-13T00:00:00Z",
    "source": "Jira REST API + OpenRouter"
  }
}
```
