# n8n Workflow Visualizer

Convert n8n workflow JSON files to visual diagrams.

## Features
- Converts n8n workflow JSON to visual diagram
- Color-coded nodes based on type (trigger/action)
- Left-to-right layout for better readability
- Exports to PNG format

## Requirements
```bash
pip install graphviz
```

Note: You also need Graphviz installed on your system:
- Windows: Download from [Graphviz Download Page](https://graphviz.org/download/)
- Linux: `sudo apt-get install graphviz`
- Mac: `brew install graphviz`

## Usage
1. Export your workflow from n8n as JSON
2. Run the script:
```bash
python workflow_visualizer.py input_workflow.json output_diagram
```

This will generate `output_diagram.png`

## Example
Input workflow JSON:
```json
{
  "nodes": [
    {
      "id": "1",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger"
    },
    {
      "id": "2",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest"
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [[{"node": "HTTP Request"}]]
    }
  }
}
```

Output:
![Example Diagram](example_diagram.png)

## Contributing
Feel free to open issues or submit pull requests!