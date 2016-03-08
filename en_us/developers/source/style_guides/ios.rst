.. highlight::objc

.. _edX Objective-C Style Guide:

###########################
EdX Objective-C Style Guide
###########################

This section describes the requirements and conventions for contributing Objective-C programming to the edX platform.

.. contents::
 :local:
 :depth: 2

**********
Principles
**********

* Favor clarity and simplicity. Remember the `principle of least surprise`_.

* Build strong interface boundaries. Sometimes this results in a little more
  code. This is okay. For example, do not expose a whole child object just to
  expose one of its properties. Instead add a trampoline method.

* Work with the compiler and type system not around it. If you are trying to
  solve a problem and there is a way to get the compiler to check it, do that.
  Once again, the shortest way to do something is not always the best way to do
  something.

* Break functionality into unit testable pieces.

* Avoid inheritance. Inheriting from some system classes, like UIViewController
  and UIView, is of course, necessary and sometimes a class hierarchy is the
  right pattern, but we strongly prefer to use composition and delegation over
  inheritance. If you are designing something with inheritance always think about
  if there's a way to change your design to not use it.

***********************
Syntax and Organization
***********************

* Follow the rules in `Apple's guidelines`_ except where they directly
  contradict what follows.

* You can automatically apply many of these formatting suggestions by typing
  ``gradle format`` into a terminal from the project root directory.

* Method names in Cocoa have a grammar. Compare the ``-getObject:atIndex:``
  method of ``NSArray`` to a hypothetical ``-get:index`` method.
  ``-getObject:atIndex:`` is much more descriptive and also sounds more natural
  in English. However, note that this is not the same grammar as English. For
  example, as described in Apple's documentation, the word ``and`` preceding an
  argument is not necessary even though it would be necessary in some cases for
  the method signature to form an English sentence.

* When in doubt, think about how something would look if it were part of one of
  Apple's core frameworks such as UIKit.

* ``#import`` declarations should be in the following groups, ordered
  alphabetically within each group:

    #. System headers (including third party libraries)
    #. Header for current file (only if in a .m file)
    #. Project headers

    For example,

    .. code-block:: objc

        // MyClass.m

        #import <FacebookSDK/FacebookSDK.h>
        #import <QuartzCore/QuartzCore.h>

        #import "MyClass.h”

        #import “OEXSomething.h”
        #import “OEXWhatever.h”


* Avoid ``#import`` in headers where possible. This makes dependencies more
  explicit and results in fewer headers included. This improves compilation
  speeds. Instead use the ``@class`` and ``@protocol`` forward declarations.

    .. code-block:: objc

        // Good
        @class SomeClass;

        @interface OtherClass
        - (instancetype)initWithSomeClass:(SomeClass*)object;
        @end


        // Bad
        #import "SomeClass.h"

        @interface OtherClass
        - (instancetype)initWithSomeClass:(SomeClass*)object;
        @end

* Avoid ``#define``. Instead use constant declarations. They are more
  accessible to the compiler. For example, "Quick Open" does not work with
  macros. Additionally, macro functions are error prone and hard to debug.
  Some examples follow:

    .. code-block:: objc

        extern NSString* const OEXExampleKey = @"OEXExampleKey";
        extern CGFloat const OEXExampleConstant = 3;

    For C macros with logic, consider if you can just use a regular function
    instead of the macro.

* Constants that are local to a single file should be declared ``static``.

* Use spaces for indentation instead of tabs. This is the Xcode default.

* Prefer properties over bare instance variables. In general, you should only
  mention an ``ivar`` in a setter for that property.

    .. code-block:: objc

        // Good
        @interface SomeClass

        @property (strong, nonatomic) NSString* foo;

        @end


        // Bad
        @interface SomeClass {
            NSString* _foo;
        }
        @end

        // Worse
        @interface SomeClass {
            NSString* foo;
        }
        @end


* Use a leading underscore to name an ``ivar``. However, you should favor
  properties and auto synthesis and almost never refer to an ``ivar`` explicitly.
  Sometimes you do need to synthesize an ``ivar`` explicitly, for example when
  implementing a protocol. Again, those should use leading underscores.

    .. code-block:: objc

        @synthesize something = _something;

* Do not bother with ``@synthesize`` for autosynthesized properties.

* Private methods do not need a leading prefix like ``_`` or ``p_``. Their
  private nature is implied by their absence from a class's header file.

* Methods added in categories to system libraries should be prefixed ``oex_``
  (for Open edX). Categories have a flat namespace. Using a prefix means our
  additions will not interfere with any other libraries.

* Follow the standard Cocoa file naming conventions:
   *  Class ``Example`` should be in ``OEXExample.[hm]``
   *  Category ``SomethingAdditions`` on class ``OEXExample``  should be in
      ``OEXExample+SomethingAdditions.[hm]``
   *  A view controller for the ``Example`` screen should be in
      ``OEXExampleViewController.[hm]``
   *  A view that displays an ``Example`` should be in ``OEXExampleView.[hm]``

*  Categories should be named for the functionality they provide.
    .. code-block:: objc

        // Good
        @interface NSString (OEXFormattingAdditions)
        //... functions that control formatting
        @end


        // Bad
        @interface NSString (OEXHelpers)
        // ... functions that do many different kinds of things
        @end


* Delegate methods should include a sender as the first argument. This allows
  the owner to distinguish which object is sending the message and sometimes to
  avoid having an extra ``ivar``.

    .. code-block:: objc

        // Good
        @interface SomeClassDelegate
        - (void)tabView:(TabView*)tabView choseTabAtIndex:(NSUInteger)index;
        @end


        // Bad
        @interface SomeClassDelegate
        - (void)choseTabAtIndex:(NSUInteger)index;
        @end

* Only put properties and methods in headers that need to be part of a class's
  interface. Everything else should be declared in a class continuation in the
  implementation file.

* Avoid lazy initialization of properties. Otherwise, it is hard to reason
  about property accesses. With lazy initialization, even read only objects
  have complicated threading behavior.

    .. code-block:: objc

        // Bad
        @interface SomeClass
        @property (strong, nonatomic) OtherClass* field;
        @end

        @implementation SomeClass

        - (OtherClass*)field {
            if(_field == nil) {
                _field = [[OtherClass alloc] init];
            }
            return _field;
        }

        @end


    Instead, add an explicit creation function like ``makeFieldIfNecessary`` or
    just instantiate it in ``-init``. For expensive things, the caller should
    have control, and for cheap things you are not gaining any performance
    advantage for the cost of decreased determinism.

* Avoid Key Value Observing. It is occasionally the only way to observe
  something, but do not design interfaces that use it. It is an `error prone API`_.

* Do not use exceptions for control flow. They should only be for top level
  failure conditions indicating programmer error. ARC is not thread safe by
  default and Swift does not even have exceptions.

* Use line comments (``//``) instead of block comments (``/* */``). They are
  easier to stack and Xcode has a keyboard shortcut for them (``⌘-/``).

* Use triple slash comments (``///``) to create inline documentation.  For
  example:

    .. code-block:: objc

        /// Method that does a thing
        - (void)someMethod { }

* Always comment the type of the contents of collection types like ``NSArray``
  and ``NSDictionary``. This makes the expectations of the code clear. For
  example:

    .. code-block:: objc

        @interface SomeClass

        /// Contents are NSString*
        @property (copy, nonatomic) NSArray* elements;
        @end

* Comparisons should be explicit for when checking pointers for null. For
  example:

    .. code-block:: objc

        // Good
        SomeObject* object = ...;
        if(object == null) {


        // Bad
        SomeObject* object = ...;
        if(!object) {

* Separate binary operands with a single space, but unary operands and casts with none.

    .. code-block:: objc

        1 + 2   // Good
        1+1     // Bad
        1+ 1    // Bad
        -3      // Good
        - 3     // Bad


* Always use braces on control structures, even if they are optional. For example:

    .. code-block:: objc

        // Good
        if(someCondition) {
            aSingleLine();
        }

        // Bad
        if(someCondition) aSingleLine();

* Properties should be marked ``nonatomic`` unless there is a very good reason
  otherwise. Marking a property ``atomic`` should signal that you have thought
  hard about the threading behavior of this property and very intentionally
  decided that it should work through ``atomic`` properties and not by
  isolating access to a queue.

* Declare memory semantics. All properties should be marked ``strong``,
  ``weak``, or ``assign``. There are defaults for different types that are
  usually right, but making it explicit forces you to think about whether
  you are creating cycles in memory.

    .. code-block:: objc

        // Good
        @property (strong, nonatomic) SomeObject* foo;

        // Bad
        @property SomeObject* foo;

*************
Writing Tests
*************

* Unit test files are typically oriented around testing a single file. The name
  of a test file should be the name of the file being tested but with the word
  ``Tests`` at the end. As an example, a test file for ``OEXSomeClass.m`` is
  ``OEXSomeClassTests.m``

* Tests should always run against test data, not a current user's. This means
  that after the tests are over, it should be as if they never ran.

* Network data should always be mocked. The tests should have the exact same
  result whether or not an Internet connection is available to the
  test runner.

* If you need to expose a method just for testing, prefix it ``t_``. This
  indicates that it should only be used by test code. This will often come up
  with view tests since their programmatic interface is often much simpler than
  their UI contract. When exposing such methods, you should ensure that a
  refactor or redesign of that view should not invalidate the test.

  For example, a login screen might have a ``t_tapLogin`` method that triggers
  the action of the login button. Even if the login screen is refactored or
  redesigned it will probably still have a login button that can be tapped so
  it is safe to make this part of the contract. However, this logic does not
  extend to the login button itself.  There are a number of ways to implement
  what appears to the user as a button, such as gesture recognizers and
  overriding ``touchesBegan:``, so exposing a ``t_loginButton`` method
  returning a ``UIButton`` would violate this rule.

* Do not redeclare a method as public inside the test. This is fragile since
  changes will not be caught by the compiler.

    .. code-block:: objc

        // Good
        // SomeClass.h
        @interface SomeClass
        @end

        @interface SomeClass (Testing)
        - (BOOL)t_isVisible;
        @end

        // SomeClass.m
        @implementation SomeClass (Testing)
        - (BOOL)t_isVisible {
            return [self isVisible];
        }
        @end


        // Bad
        // SomeClass.h
        @interface SomeClass
        @end

        // SomeClass.m
        @implementation SomeClass
        - (void)isVisible {
            ...
        }
        @end

        // SomeClassTests.m
        @interface SomeClass (Testing)
        - (void)isVisible;
        @end


.. _Apple's guidelines: https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Conventions/Conventions.html
.. _error prone API: http://khanlou.com/2013/12/kvo-considered-harmful/
.. _principle of least surprise: http://en.wikipedia.org/wiki/Principle_of_least_astonishment

