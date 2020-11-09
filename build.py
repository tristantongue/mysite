pages = [
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title": "Tristan Tongue",
        },
        {
            "filename": "content/about.html",
            "output": "docs/about.html",
            "title": "About Me",
        },
        {
            "filename": "content/experience.html",
            "output": "docs/experience.html",
            "title": "Experience - Tristan Tongue",
        },
        {
            "filename": "content/musicpost.html",
            "output": "docs/musicpost.html",
            "title": "The Mathematical Relationships of Music",
        },
        {
            "filename": "content/schiller.html",
            "output": "docs/schiller.html",
            "title": "Aesthetics in Schiller and Schopenhauer",
        },
    ]
#build template function reads in base template, replaces the title palceholder with the arg, and returns the ready to be used template
def build_template(pagetitle):
    template = open('templates/base.html').read()
    ready_template = template.replace("{{title}}", pagetitle)
    return ready_template
#build page function take the args of template and content, and replaces the content placeholder with a content page
def build_page(template, content):
    finished_page = template.replace("{{content}}", content)
    return finished_page

def main():
    print('building static site')

    
    for page in pages:
        page_content = page['filename']
        page_title = page['title']
        page_output = page['output']

        template = build_template(page_title)
        content = open(page_content).read()
        finished_page = build_page(template, content)
        open(page_output, "w+").write(finished_page)


if __name__ == "__main__":
    main()