#!/usr/bin/env python

import io
import pypandoc
import panflute


def prepare(doc):
	doc.images = []
	doc.links = []
	doc.tables = []

def action(elem, doc):
    if isinstance(elem, panflute.Image):
        doc.images.append(elem)
    elif isinstance(elem, panflute.Link):
        doc.links.append(elem)
    elif isinstance(elem, panflute.Table):
        doc.tables.append(elem)

if __name__ == '__main__':
    data = pypandoc.convert_file('../README.md', 'json')
    doc = panflute.load(io.StringIO(data))

    #print(doc)
#    print(data)

    doc.images = []
    doc.links = []
    doc.tables = []
    doc = panflute.run_filter(action, prepare=prepare, doc=doc)

    print("\nList of tables:")
    for tables in doc.tables:
        print(tables)

