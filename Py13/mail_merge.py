def mail_merge(names, template):
    t = open(template).read()
    return [t.replace("<name>", name.strip()) for name in open(names)]