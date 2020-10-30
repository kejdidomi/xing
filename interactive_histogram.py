class Histogram:
    def __init__(self, content=[]):
        self.content = content

    def show(self, k=1):
        a = self.content
        print("Element\tValue\tHistogram")
        for i in range(len(a)):
            print(str(i+1) + "\t\t" + str(a[i]) + "\t\t" + "*" * (a[i]//k))

a = [1,2,3]
b = Histogram(a)
b.show()