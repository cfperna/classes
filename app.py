class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 10)+1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("horse")
cloud.add("horse")
cloud.add("1")
print(cloud.tags)
print(cloud.__getitem__('python'))
