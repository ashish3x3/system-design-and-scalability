

Sometimes the problem that you’re solving is as simple as “I don’t have the interface that I want
.”

Two of the patterns in Design Patterns solve this problem:

Adapter takes one type and produces an interface to some other type.

Façade creates an interface to a set of classes, simply to provide a more comfortable way to deal
 with a library or bundle of resources.


 Adapter
 When you’ve got this, and you need that, Adapter solves the problem.
 The only requirement is to produce a that, and there are a number of ways you can accomplish this adaptation:

 Important points about Adapter Pattern
 one of the key benefits of using Adapter pattern in Java is reusing code, making incompatible interfaces work together and loose coupling because Adapter tends to encapsulate incompatible interface quite well.

 Adapter design pattern ensures code reusability for delegating calls from the client to original class, i.e. it act like a wrapper of original interface, that's why it's also called wrapper pattern or simply a wrapper.

 One of the cases where you want to use Adapter design pattern in Java program is while using a third-party library. By making sure, your program uses Adapter, which is in your control, rather than directly using third-party interface and classes, you can anytime replace third-party library, with similar, better performing API. You can count this one of the pros of using Adapter pattern.

 Adapter just converts one interface to another, without adding additional functionalities, while Decorator adds new functionality into an interface.


 You can also use Adapter design pattern in Java for conversion classes, e.g. Suppose your client do all calculation in Miles and the library you are using expects Kilometers. In this case, you can write an Adapter class, which takes miles from Client, converts it to Kilometer and leverages external library methods for all calculation. While returning a result, it can convert KM back to miles and send the result to Client.

 Prefer Object-based Adapter design pattern than Class based, because former uses Composition for code re-use and more flexible than Inheritance based approach of Class based Adapter pattern


 There are two ways to implement Adapter design pattern in Java, one using Inheritance also known as Class Adapter pattern and other is using Composition, better known as Object Adapter pattern. In both cases, it's better to declare client interacting public methods in an interface, you may call it target interface.
 One advantage of using target interface to wrap client facing method in an Adapter, you create a loosely coupled design, where you can replace your Adapter with better implementation in the later stage of development.

 Now your Class Adapter pattern extends the original interface, which is incompatible to the client but provides the functionality needed by the client, and it also implements the target interface. Now, Adapter implements target method in such a way that it delegates actual work on original class, which Adapter get access by extending it.

 Similarly, in the case of Object Adapter pattern, which uses Composition for reusing code, it also implements target interface and uses object of the Original incompatible class to do all of its work. Since It's better to prefer composition over inheritance, I advise that you should stick with Object Adapter pattern.







 Adapter just converts one interface to another, without adding additional functionalities, while Decorator adds new functionality into an interface.

 Read more: http://javarevisited.blogspot.com/2016/08/adapter-design-pattern-in-java-example.html#ixzz55MwcnDl2
 # ChangeInterface/Adapter.py
 # Variations on the Adapter pattern.

 class WhatIHave:
     def g(self): pass
     def h(self): pass

 class WhatIWant:
     def f(self): pass

 class ProxyAdapter(WhatIWant):
     def __init__(self, whatIHave):
         self.whatIHave = whatIHave

     def f(self):
         # Implement behavior using
         # methods in WhatIHave:
         self.whatIHave.g()
         self.whatIHave.h()

 class WhatIUse:
     def op(self, whatIWant):
         whatIWant.f()

 # Approach 2: build adapter use into op():
 class WhatIUse2(WhatIUse):
     def op(self, whatIHave):
         ProxyAdapter(whatIHave).f()

 # Approach 3: build adapter into WhatIHave:
 class WhatIHave2(WhatIHave, WhatIWant):
     def f(self):
         self.g()
         self.h()

 # Approach 4: use an inner class:
 class WhatIHave3(WhatIHave):
     class InnerAdapter(WhatIWant):
         def __init__(self, outer):
             self.outer = outer
         def f(self):
             self.outer.g()
             self.outer.h()

     def whatIWant(self):
         return WhatIHave3.InnerAdapter(self)

 whatIUse = WhatIUse()
 whatIHave = WhatIHave()
 adapt= ProxyAdapter(whatIHave)
 whatIUse2 = WhatIUse2()
 whatIHave2 = WhatIHave2()
 whatIHave3 = WhatIHave3()
 whatIUse.op(adapt)
 # Approach 2:
 whatIUse2.op(whatIHave)
 # Approach 3:
 whatIUse.op(whatIHave2)
 # Approach 4:
 whatIUse.op(whatIHave3.whatIWant())


 I’m taking liberties with the term “proxy” here, because in Design Patterns they assert that a proxy must have an identical interface with the object that it is a surrogate for. However, if you have the two words together: “proxy adapter,” it is perhaps more reasonable.




 Façade
 A general principle that I apply when I’m casting about trying to mold requirements into a first-cut object is “If something is ugly, hide it inside an object.” This is basically what Façade accomplishes. If you have a rather confusing collection of classes and interactions that the client programmer doesn’t really need to see, then you can create an interface that is useful for the client programmer and that only presents what’s necessary.

 Façade is often implemented as singleton abstract factory. Of course, you can easily get this effect by creating a class containing static factory methods:



 # ChangeInterface/Facade.py
 class A:
     def __init__(self, x): pass
 class B:
     def __init__(self, x): pass
 class C:
     def __init__(self, x): pass

 # Other classes that aren't exposed by the
 # facade go here ...

 class Facade:
 	 @staticmethod
     def makeA(x):
     	return A(x)

 	 @staticmethod
     def makeB(x):
     	return B(x)

     def makeC(x): return C(x)
     # Note that some code might use the old method of defining a static method, using staticmethod as a function rather than a decorator. This should only be used if you have to support ancient versions of Python (2.2 and 2.3)
     makeC = staticmethod(makeC)

 # The client programmer gets the objects
 # by calling the static methods:
 a = Facade.makeA(1);
 b = Facade.makeB(1);
 c = Facade.makeC(1.0);























