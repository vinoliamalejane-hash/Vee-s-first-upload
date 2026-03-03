# edge_tabs_output.py
# Script to display Edge browser tabs metadata

edge_all_open_tabs = [
    {
        "pageTitle": "File",
        "pageUrl": "https://ethuto.cut.ac.za/ultra/courses/_30829_1/outline/file/_1585333_1",
        "tabId": 1337674578,
        "isCurrent": True
    }
]

def show_tabs_info(tabs):
    for tab in tabs:
        status = "Active tab (currently being viewed)" if tab["isCurrent"] else "Background tab"
        print(f"Tab ID: {tab['tabId']}")
        print(f"Title: {tab['pageTitle']}")
        print(f"URL: {tab['pageUrl']}")
        print(f"Status: {status}")
        print("-" * 50)

# Run the function
show_tabs_info(edge_all_open_tabs)
