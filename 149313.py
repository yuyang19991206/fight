
# coding: utf-8

# # Python面向对象编程
# 
# 在本文中，您将学习Python中的OOP的以下基本概念：
# 
# * Python类
# * 对象实例
# * 定义和使用方法
# * OOP继承

# # 什么是面向对象编程（OOP）？
# 
# 面向对象编程（Object-oriented Programming，简称OOP）是一种编程范例，它提供了一种结构化程序的方法，以便将属性和行为捆绑到单个对象中。
# 
# 例如，对象可以表示具有姓名属性，年龄，地址等的人，具有行走，说话，呼吸和跑步等行为。或者包含收件人列表，主题，正文等属性的电子邮件，以及添加附件和发送等行为。
# 
# 换句话说，面向对象编程是一种用于建模具体的，现实世界的事物，如汽车以及公司和员工，学生和教师等事物之间的关系的方法.OOP将现实世界的实体建模为软件对象，一些与之相关的数据，可以执行某些功能。
# 
# 另一种常见的编程范例是函数式编程，其构造类似于顺序执行的程序，因为它以函数和代码块的形式提供一组步骤，这些步骤顺序地流动以完成任务。
# 
# 关键的一点是，对象是面向对象编程范例的核心，不仅在函数编程中表示数据，而且在程序的整体结构中也是如此。
# 
# >注意：由于Python是一种多范式编程语言，您可以选择最适合手头问题的范例，在一个程序中混合使用不同的范例，和/或随着程序的发展从一种范例切换到另一种范例。

# # Python中的类
# 
# 首先关注数据，每个事物或对象都是某个类的实例。
# 
# Python中可用的原始数据结构（如数字，字符串和列表）旨在分别表示简单的事物，例如某事物的成本，诗歌的名称和您喜欢的颜色。
# 
# 如果你想代表更复杂的东西怎么办？
# 
# 例如，假设您想跟踪许多不同的动物。如果您使用了列表，则第一个元素可以是动物的名称，而第二个元素可以表示其年龄。
# 
# 你怎么知道哪个元素应该是哪个？如果你有100种不同的动物怎么办？你确定每只动物都有名字和年龄，等等吗？如果你想为这些动物添加其他属性怎么办？这缺乏组织，这是课程的确切需要。
# 
# 类用于创建新的用户定义数据结构，其中包含有关某些内容的任意信息。对于动物，我们可以创建一个Animal（）类来跟踪关于Animal的属性，如名称和年龄。
# 
# 重要的是要注意一个类只提供结构 - 它是应该如何定义某个东西的蓝图，但它实际上并不提供任何真实的内容。 Animal（）类可以指定名称和年龄是定义动物所必需的，但它实际上不会说明特定动物的名字或年龄。
# 
# 将类视为应该如何定义某事的想法可能会有所帮助

# # Python对象（实例）
# 
# 虽然类是蓝图，但实例是具有实际值的类的副本，字面上是属于特定类的对象。这不再是一个想法;它是一只真正的动物，就像一只名叫罗杰的狗，已经八岁了。
# 
# 换句话说，课程就像一个表格或问卷。它定义了所需的信息。填写表格后，您的特定副本就是该课程的一个实例;它包含与您相关的实际信息。
# 
# 您可以填写多个副本以创建许多不同的实例，但如果没有表单作为指导，您将会丢失，而不知道需要哪些信息。因此，在创建对象的单个实例之前，我们必须首先通过定义类来指定所需的内容。
# 
# # 如何在Python中定义类
# 
# 在Python中定义类很简单：
# 
# ```
# class Dog:
#     pass
# ```
# 
# 
# 首先使用class关键字指示您正在创建一个类，然后添加该类的名称（使用骆驼命名法，以大写字母开头。）
# 
# 另外，我们在这里使用了Python关键字pass。这经常被用作代码最终会占用的占位符。它允许我们运行此代码而不会抛出错误。
# 
# 
# >注意：上面的代码在Python 3上是正确的。在Python 2.x（“遗留Python”）上，您将使用稍微不同的类定义：
# >```
# >＃Python 2.x类定义：
# >class Dog（object）：
# >    Pass
# >```
# >括号中的（对象）部分指定了您继承的父类（更多内容见下文。）在Python 3中，这不再是必需的，因为它是隐式默认值。

# 
# # 实例属性
# 
# 所有类都创建对象，所有对象都包含称为属性的特征（在开头段落中称为属性）。使用__init __（）方法通过为对象的初始属性提供其默认值（或状态）来初始化（例如，指定）对象的初始属性。此方法必须至少有一个参数以及自变量，它引用对象本身（例如，Dog）。
# 
# ```
# class Dog:
# 
#     # Initializer / Instance Attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# ```
# 
# 在我们的Dog（）类中，每只狗都有一个特定的名字和年龄，这对于你何时开始真正创造不同的狗来说显然很重要。请记住：该类程仅用于定义狗，而不是实际创建具有特定名称和年龄的个体狗的实例;我们很快就会谈到这一点。
# 
# 类似地，自变量也是类的实例。由于类的实例具有不同的值，我们可以声明Dog.name = name而不是self.name = name。但由于并非所有狗都拥有相同的名称，我们需要能够为不同的实例分配不同的值。因此需要特殊的自变量，这将有助于跟踪每个类的各个实例。
# 
# 
# >注意：您永远无需主动调用__init __（）方法;当你创建一个新的'Dog'实例时会自动调用它。

# # 类属性
# 
# 虽然实例属性特定于每个对象，但类属性对于所有实例都是相同的 - 在这种情况下，属性都来自狗。
# 
# ```
# class Dog:
# 
#     # Class Attribute
#     species = 'mammal'
# 
#     # Initializer / Instance Attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
# ```
# 因此，虽然每只狗都有一个独特的名字和年龄，但每只狗都是哺乳动物。
# 
# 让我们创造一些狗......
# 
# 
# # 实例化对象
# 实例化是创建一个新的，唯一的类实例的意思。
# 
# ```
# >>> class Dog:
# ...     pass
# ...
# >>> Dog()
# <__main__.Dog object at 0x1004ccc50>
# >>> Dog()
# <__main__.Dog object at 0x1004ccc90>
# >>> a = Dog()
# >>> b = Dog()
# >>> a == b
# False
# ```
# 
# 我们首先定义一个新的Dog（）类，然后创建两个新的狗，每个狗分配给不同的对象。因此，要创建类的实例，请使用类名，后跟括号。然后为了证明每个实例实际上是不同的，我们实例化了两个狗，将每个狗分配给一个变量，然后测试这些变量是否相等。
# 
# 您认为类实例的类型是什么？
# 
# ```
# >>> class Dog:
# ...     pass
# ...
# >>> a = Dog()
# >>> type(a)
# <class '__main__.Dog'>
# ```
# 
# 
# 让我们看一个稍微复杂的例子.....
# 
# 

# In[1]:


class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))


# >注意：请注意我们如何使用点表示法来访问每个对象的属性。

# ## 这是怎么回事？
# 
# 我们创建了Dog（）类的新实例，并将其分配给变量philo。然后我们通过了两个论点，“Philo”和5，分别代表狗的名字和年龄。
# 
# 这些属性将传递给__init__方法，该方法在您创建新实例时将其调用，并将名称和年龄附加到对象。您可能想知道为什么我们不必传递自我论证。
# 
# 这是Python魔法: 当你创建一个新的类实例时，Python会自动确定self是什么（在本例中是一个Dog）并将其传递给__init__方法。
# 
# ## 练习
# 
# >用相同的Dog类，实例化三只新狗，每只狗的年龄不同。然后编写一个名为get_biggest_number（）的函数，它接受任意数量的年龄并返回最旧的函数。然后输出最老的狗的年龄.

# # 实例方法
# 
# 实例方法在类中定义，用于获取实例的内容。
# 
# 它们还可用于使用对象的属性执行操作。与__init__方法一样，第一个参数始终是self：

# In[2]:


class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))


# 在后一种方法中，我们定义了行为speak（）。您可以为狗分配哪些其他行为？回顾一下开头的段落，看看其他对象的一些示例行为。

# ## 修改属性
# 
# 您可以根据某些行为更改属性的值：
# 

# In[3]:


class Email:
    def __init__(self):
        self.is_sent = False
    def send_email(self):
        self.is_sent = True
        
my_email = Email()
print(my_email.is_sent)

my_email.send_email()
print(my_email.is_sent)


# 在这里，我们添加了一种发送电子邮件的方法，该方法将is_sent变量更新为True。
# 
# # Python对象继承
# 继承是一个类采用另一个类的属性和方法的过程。新形成的类称为子类，子类派生的类称为父类。
# 
# 重要的是要注意子类覆盖或扩展父类的功能（例如，属性和行为）。换句话说，子类继承了父项的所有属性和行为，但也可以指定要遵循的不同行为。最基本的类是一个对象，通常所有其他类都继承为它们的父对象。
# 
# 定义新类时，Python 3隐式使用object作为父类。所以以下两个定义是等价的：
# 
# ```
# class Dog(object):
#     pass
# 
# # In Python 3, this is the same as:
# 
# class Dog:
#     pass
# ```
# 
# 
# >注意：在Python 2.x中，新风格类和旧风格类之间存在区别。不在这里详细介绍，但是通常希望您将对象指定为父类，以确保在编写Python 2 OOP代码时定义新样式类。
# 
# # 狗公园示例
# 
# 让我们假装我们在一个狗公园。有多个Dog对象参与Dog行为，每个对象都有不同的属性。一般来说，这意味着有些狗正在跑步，而有些正在伸展，有些正在盯着其他狗。此外，每只狗都由它的主人命名，并且由于每只狗都是活生生的, 各个年龄段的都有。
# 
# 将一只狗与另一只狗区分开来的另一种方法是什么？狗的品种怎么样：

# In[4]:


class Dog:
    def __init__(self, breed):
        self.breed = breed

spencer = Dog("German Shepard")
print(spencer.breed)

sara = Dog("Boston Terrier")
print(sara.breed)


# 
# 每种犬的行为略有不同。考虑到这些因素，让我们为每个品种创建单独的类。这些是父类Dog的子类。
# 
# ## 扩展父类的功能
# 运行下方代码：

# In[5]:


class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))


# 
# 在您完成此程序时，请仔细阅读，以帮助您了解正在发生的事情，然后在运行程序之前，查看您是否可以预测预期的输出。
# 
# 我们没有添加任何特殊属性或方法来区分RussellTerrier和Bulldog，但由于它们现在是两个不同的类，我们可以为它们提供定义各自速度的类属性。
# 
# 
# 
# # 父类与子类
# isinstance（）函数用于确定实例是否也是某个父类的实例。
# 
# 

# In[6]:


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# Is julie and instance of jim?
print(isinstance(julie, jim))


# 
# 看得懂吗？ jim和julie都是Dog（）类的实例，而johnnywalker不是Bulldog（）类的实例。然后作为一个完整性检查，我们测试了julie是否是jim的实例，这是不可能的，因为jim是类的实例而不是类本身 - 因此是TypeError的原因。
# 
# ##  覆盖父类的功能
# 请记住，子类也可以覆盖父类的属性和行为。举些例子：

# In[7]:


class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
     species = 'reptile'

frank = SomeBreed()
print(frank.species)

beans = SomeOtherBreed()
print(beans.species)


# SomeBreed（）类从父类继承物种，而SomeOtherBreed（）类覆盖物种，将其设置为爬行动物~~~~~~~~
# 
# # 练习: 狗狗继承
# 创建一个容纳狗的实例的Pets类;这个类与Dog类完全分开。换句话说，Dog类不会继承Pets类。然后将三个dog实例分配给Pets类的实例。从下面的代码开始。将文件另存为pets_class.py。您的输出应如下所示：
# 
# >I have 3 dogs.
# >
# >Tom is 6. 
# >
# >Fletcher is 7. 
# >
# >Larry is 9. 
# >
# >And they're all mammals, of course.
# 
# # 练习: 狗狗饿不饿
# 
# 使用相同的文件，将一个实例属性is_hungry = True添加到Dog类。然后添加一个名为eat（）的方法，在调用时将is_hungry的值更改为False。找出喂养每只狗的最佳方式，然后输出“我的狗饿了。”如果所有人都饿了或“我的狗不饿”。如果所有人都不饿。最终输出应如下所示：
# 
# >I have 3 dogs. 
# >
# >Tom is 6. 
# >
# >Fletcher is 7. 
# >
# >Larry is 9. 
# >
# >And they're all mammals, of course. 
# >
# >My dogs are not hungry.

# 
# # 结论
# 
# 您现在应该知道哪些类是什么，为什么您想要或需要使用它们，以及如何创建父类和子类以更好地构建程序。
# 
# 请注意，OOP是一种编程范例，而不是Python概念。大多数现代编程语言，如Java，C＃，C ++都遵循OOP原则。所以好消息是学习面向对象的编程基础知识对你来说在各种情况下都很有价值 - 无论你是否使用Python

# In[15]:


#在这里完成例6-1的程序调试
class Person(object):
    def __init__(self,name='',age=20,sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
        
    def setName(self,name):
        if not isinstance(name,str):
            raise Exception('name must be a string.')
        self.__name=name
        
    def setAge(self,age):
        if type(age)!=int:
            raise Exception('age must be an integer.')
        self.__age=age
        
    def setSex(self,sex):
        if sex not in('man','woman'):
            raise Exception('sex must be "man" or "woman"')
        self.__sex=sex
        
    def show(self):
        print(self.__name,self.__age,self.__sex,sep='\n')
        
        
    #派生类
class Teacher(Person):
    def __init__(self,name='',age=30,sex='man',department='Computer'):
        super(Teacher,self).___init__(name,age,sex)
        self.setDepartment(department)
            
    def setDepartment(self,department):
        if type(department)!=str:
            raise Exception('department must be a string.')
        self.__department=__department
            
    def show(self):
        super(Teacher,self).show()
        print(self.__department)
            
if __name__=='__main__':
    zhangsan=Person('Zhang San',19,'man')
    zhangsan.show()
    print('='*30)
        
    lisi=Teacher('Li Si',32,'man','Math')
    lisi.show()
    lisi.setAge(40)
    lisi.show()



# In[18]:


#在这里完成例6-2的程序调试
class Deque:
    def __init__(self,iterable=None,maxlen=10):
        if iterable==None:
            self._content=[]
            self._current=0
        else:
            self._content=list(iterable)
            self._current=len(iterable)
        self._size+maxlen
        if self._size<self._current:
            self._size=self._current
            
    # 析构方法
    def __del__(self):
        del self._content

    # 修改队列大小
    def setSize(self, size):
        if size < self._current:
            # 缩小对列，同时删除后边的元素
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    # 右侧入站
    def appendRight(self, v):
        if self._current < self._size:
            self._content.append(v)     # 使用追加方法
            self._current = self._current + 1
        else:
            print('The queue is full.')

    # 左侧入站
    def appendLeft(self, v):
        if self._current < self._size:
            self._content.insert(0, v)   # 使用插入方法
            self._current = self._current + 1
        else:
            print('The queue is full.')

    # 左侧出站
    def popLeft(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)   # pop,弹出索引所指数据,并返回该数据.默认弹出最后一个
        else:
            print('The queue is empty.')

    # 右侧出站
    def popRight(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('The queue is empty.')

    # 循环移位
    def rorate(self, k):
        if abs(k) > self._current:
            print('k must <=' + str(self._current))
            return
        self._content = self._content[-k:] + self._content[:-k]

    # 元素翻转
    def reverse(self):
        self._content = self._content[::-1]

    # 显示当前对列元素的个数
    def __len__(self):
        return self._current

    # 显示当前队列中的元素
    def __str__(self):
        return 'Deque(' + str(self._content) + ',maxlen=' + str(self._size) + ')'

    # 队列置空
    def clear(self):
        self._content = []
        self._current = 0

    # 测试队列是否为空
    def isEmpty(self):
        return not self._content

    # 测试队列是否已满
    def isFull(self):
        return self._current == self._size


if __name__ == '__main__':
    print('Please use the file as a module that deque.')


# In[23]:


#在这里完成例6-3的程序调试
class Stack:
    def __int__(self,maxlen=10):
        self._content=[]
        self._size=maxlen
        self._current=0

    def __del__(self):
        del self._content
        
    def clear(self):
        self._content=[]
        self._current=0
        
    def isEmpty(self):
        return not self._content
        
    def setSize(self,size):
        if size<self._current:
            print('new size must >=' +str(self._current))
            return
        self._size=size
        
    def isFull(self):
        return self._current==self._size
        
    def push(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current=self._currnet+1
        else:
            print('Stack is Full!')
            
        def pop(self):
            if self._content:
                self._current=self._current-1
                return self._content.pop()
            else:
                print('Stack is empty!')
                
        def __str__(self):
            return 'Stack('+Str(self._content)+',maxlen='+str(self._size)+')'
            
        __repr__=__sttr__    
            
            


# In[10]:


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.is_hungry = True
        
    def description(self):
        return "{} is {} years old.".format(self.name,self.age)
    def eat(self):
        self.is_hungry=False
dogs=[
Dog("Tom",6),
Dog("Fletcher",7),
Dog("Larry",9)]

class Pets:
    def __init__(self,dogs):
        self.Pdogs=dogs
    def isHungry(self):
        if(any([i.is_hungry for i in self.Pdogs])):
            print("My dogs are hungry.")
        else:
            print("My dogs are not hungry.")
    def feedingAll(self):
        for i in self.Pdogs:
            i.eat()
pets=Pets(dogs)
print("I have {} dogs.".format(len(dogs)))
for i in pets.Pdogs:
    print(i.description())
print("And they're all mammals, of course.")
pets.feedingAll()
pets.isHungry()
    
        

