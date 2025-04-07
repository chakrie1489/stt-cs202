import json
import networkx as nx

with open("dependencies.json", "r") as file:
    dependencies = json.load(file)
G = nx.DiGraph()
fan_in = {mod: 0 for mod in dependencies}
fan_out = {mod: len(dependencies[mod].get("imports", [])) for mod in dependencies}

for mod, data in dependencies.items():
    for imported in data.get("imports", []):
        G.add_edge(imported, mod)
        fan_in[imported] += 1

core_module = max(fan_in, key=fan_in.get)
affected_modules = nx.descendants(G, core_module)
high_risk_modules = [mod for mod in dependencies if fan_out[mod] > len(dependencies) // 10]
with open("dependency_analysis_output.txt", "w") as output_file:
    # Core Module
    output_file.write(f"=== Core Module Identified: {core_module} ===\n")
    output_file.write(f"Imported by {fan_in[core_module]} modules. Changes here may affect:\n")
    if affected_modules:
        output_file.write("\n".join(affected_modules) + "\n")
    else:
        output_file.write("No direct dependencies found.\n")

    # High-Risk Modules
    output_file.write("\n=== High-Risk Modules (If Modified, May Break the System) ===\n")
    if high_risk_modules:
        output_file.write("\n".join(high_risk_modules) + "\n")
    else:
        output_file.write("No high-risk modules found.\n")

