from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os

def generate_report(repo_name, commits):
    templates_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("report.html")

    html = template.render(
        repo_name = repo_name,
        commits=commits,
        generated_at=datetime.now().strftime("%Y-%m-%D %H:%M:%S")
    )

    output_path = "commit-reviwer-report.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Report successfully written to {output_path}")
    return output_path