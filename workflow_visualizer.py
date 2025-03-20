import json
import argparse
from graphviz import Digraph

class N8nWorkflowVisualizer:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.workflow = json.load(f)
        
        self.dot = Digraph(comment='N8N Workflow')
        self.dot.attr(rankdir='LR')  # Left to Right layout
        
    def _add_node_style(self, node_type):
        """Define node styles based on type"""
        styles = {
            'trigger': {'color': '#4CAF50', 'shape': 'rectangle'},
            'action': {'color': '#2196F3', 'shape': 'rectangle'},
            'default': {'color': '#9E9E9E', 'shape': 'rectangle'}
        }
        return styles.get(node_type, styles['default'])
    
    def generate_diagram(self):
        # Add nodes
        for node in self.workflow['nodes']:
            node_id = node['id']
            node_name = node['name']
            node_type = 'trigger' if 'Trigger' in node['type'] else 'action'
            
            style = self._add_node_style(node_type)
            self.dot.node(
                str(node_id),
                node_name,
                style='filled',
                fillcolor=style['color'],
                shape=style['shape']
            )
        
        # Add connections
        for conn in self.workflow['connections'].items():
            source = conn[0]
            for target_list in conn[1]['main']:
                for target in target_list:
                    self.dot.edge(source, str(target['node']))
    
    def save(self, output_file):
        """Save diagram to file"""
        self.dot.render(output_file, format='png', cleanup=True)

def main():
    parser = argparse.ArgumentParser(description='Convert n8n workflow JSON to visual diagram')
    parser.add_argument('input_file', help='Input JSON workflow file')
    parser.add_argument('output_file', help='Output diagram file (without extension)')
    
    args = parser.parse_args()
    
    visualizer = N8nWorkflowVisualizer(args.input_file)
    visualizer.generate_diagram()
    visualizer.save(args.output_file)

if __name__ == '__main__':
    main()