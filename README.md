# github-crawler

[Object Oriented Tricks](https://hackernoon.com/tagged/oot)

[SpotBugs rules](https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html)

关键词 bad practice 搜索到的 pull requests 更有可能包含解释

issues 也很有用的样子，但是我只爬了 prs

[https://github.com/search?l=Java&q="bad+practice"&state=closed&type=Issues](https://github.com/search?l=Java&q="bad+practice"&state=closed&type=Issues)

1.  bad use of static method in a non static way:
    https://github.com/openjdk/panama-foreign/pull/125

4.  using default package:
    https://github.com/Shrined/Group-project-1/pull/20

6.  sending name and server version(security)
    https://github.com/igniterealtime/Openfire/pull/1584

7.  Absolute path on file, this is bad practice. Need use relative path

    https://github.com/GSU-Gromyko/GSU-Java/pull/7

13.  Executors.newSingelThreadExecutor(), this is bad practice because it uses an unmanaged thread. Instead, we should use a ManagedExecutor from MP Context Propagation
     https://github.com/OpenLiberty/draft-guide-reactive-service-testing/issues/10
15.  specifying the broadcaster permission. (与外界交互的权限可能会涉及安全问题，类似的还有  Activity 和 ContentProvider)
     https://github.com/zxing/zxing/issues/1245
16.  The use of swing together with JavaFX is bad prac [stackoverflow](https://stackoverflow.com/questions/22487345/swing-timer-alternative-for-javafx-and-the-thread-management-difference)  (Java 限定)
     https://github.com/Wiggyboy/limn/issues/1

#### 待分类

2.  [Python] missing close for open, 尤其是 `for line in open(\"filename\")`, 最好采用 with-open-as 的写法

    https://api.github.com/repos/wxWidgets/Phoenix/issues/1572

4.  [Python] using `self.__class__` in the `super()` call, Python3 complains about argument passing from the Child Class [原因](https://stackoverflow.com/questions/19776056/the-difference-between-super-method-versus-superself-class-self-method/19776143#19776143)

    https://api.github.com/repos/rbnvrw/nd2reader/issues/33

5.  [Python] inject new args in the middle position

    https://api.github.com/repos/sosw/sosw/issues/197

6.  Loops, try-catch statements, etc. are bad practice within constructor. The constructor purpose is only to initialize class fields and nothing else.

    https://github.com/ivaylomitev17/shop-black-friday/pull/3

7.  loop nesting more than 3 is bad practice (但代码是 if-for-if 这样的三层)

    https://github.com/petrZhilitsky/test/pull/1

8.  Suspicious reference comparison of Boolean values, Spotbugs rule `RC_REF_COMPARISON_BAD_PRACTICE_BOOLEAN` 

    https://github.com/apache/druid/pull/8076

8.  use setter methods (overridable) in the constructor

    https://github.com/AY1920S1-CS2103T-T13-1/main/pull/177

10. [Python] use of os.errno is considered bad practice (not supported in 3.6 and onwards), while importing errno explicitly and using it is better

    https://github.com/Belval/pdf2image/pull/89

11. Negating the result of compareTo()/compare() (SpotBugs RV_NEGATING_RESULT_OF_COMPARETO)

    https://github.com/jenkinsci/jenkins/pull/4237

12. in general use [@Autowired](https://github.com/Autowired) with setters is very bad practice

    https://github.com/eRudych/taskTest/pull/2

12. don't use finalize [reason](https://howtodoinjava.com/java/basics/why-not-to-use-finalize-method-in-java/)

    https://github.com/CorfuDB/CorfuDB/pull/1804

13. Declaring a variable only to immediately return or throw it is a bad practice (Sonar)

    https://github.com/qjx378/wenku/pull/3

14. 

15. 





### 大致分类

#### import *

1.  import *
    https://github.com/mkamadeus/OOP-Avatar-Duel/issues/6

2.  [python] import *  [why](https://www.asmeurer.com/removestar/)

    其他意见: import * is bad as a public API, but it is fine as an implementation details.
    https://github.com/webpy/webpy/pull/605

3.  using "star" imports is bad practice, it is better to import specific modules.

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/634

4.  wildcard imports are bad practice 

    https://github.com/RiiConnect24-Bot/RC24-Bot/pull/92

5.  [Python] wildcard imports are considered bad practice

    https://github.com/tue-robotics/tue_robocup/pull/1006

6.  [Python] bad practice to use star imports 

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/535

7.  [Python] star imports

    https://github.com/Unity-Technologies/ml-agents/pull/2584/files

8. Avoid to import star which is a bad code practice

   https://github.com/apache/calcite/pull/1910

9. wildcard import

   https://github.com/HongyuHe/text-adventure/pull/7

10. using glob import was considered a bad practice

    https://github.com/thewca/tnoodle-lib/pull/5

11. [Python] avoid using star imports - this is a bad practice

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/442

12. [Python] avoid using star imports - it's a bad practice

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/467

13. [Python] import * is a bad practice

    https://github.com/j-abc/opensongshare/pull/2

14. bad practice to import with *

    https://github.com/YulianaYershova/notification_service/pull/1/files/8794df8bcecea821bbfdcadece068dcda87d0525#diff-43023f022e956f56887190f2e1a2d399

15. [Python] avoid using star imports (bad practice)

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/401

16. [Python] avoid using star imports (bad practice)

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/392

17. 

#### while true

1.  https://github.com/robdesautel/learning/issues/4

2.  [Python]  hard to tell the condition required to break the loop (学生作业)

    https://api.github.com/repos/StormJones/JCU_ProgrammingTwo/issues/2

#### nullcheck

##### chained set of calls

1.  bad practice where function call was in return statement. (Now handles null case) 
    https://github.com/Duelers/Duelers/pull/24

2.  A chained set of calls: NPE (Null Pointer Exception) prone, difficult to read, painful when you run in a NPE and don't know which part caused it

    https://api.github.com/repos/hazelcast/hazelcast/issues/1612

3. bad practice to use get() for Optional without any check that value actually exists

   https://github.com/SilinPavel/cloud-pipeline/pull/27

4. 

#### return type

1.  bad practice to return sometimes \"null\" and sometimes not. 当方法头部声明返回值类型为 List时，默认空值最好返回empty list，而不是null

    https://api.github.com/repos/diennea/bookkeeper-visual-manager/issues/60

2.  [Python] return different types of things in different cases

    https://api.github.com/repos/SciTools/iris/issues/3694

3.  Returning nulls is a bad practice when you need to return a collections

    https://github.com/Vlavladada/IOProject1/pull/1

4.  Method with Boolean return type returns explicit null

    https://github.com/apache/fineract/pull/696

5.  

#### assertions

1.  use assertnull, use assertfalse:
    https://github.com/corona-code-monkeys/soccer-association-system/pull/57

2.  bad practice to make assertions based on toString.有原因和建议做法

    https://github.com/Zolikon/CodingPractice/issues/7

#### Exceptions

1.  [Python] pokemon-exception catching is a bad practice `except Exception:` 

    https://github.com/open-zaak/open-zaak/pull/535

3.  throw render.createPDF()'s IOException instead of general Exception 
    https://github.com/danfickle/openhtmltopdf/issues/406

4.  [Python] Never do an `except Exception`. This is a bad practice since you catch ALL the potential exception, and we may lose something import 

    https://github.com/ansible/ansible/pull/65348

5.  [Python] Catching everything and then passing is very bad practice

     https://github.com/ModOrganizer2/modorganizer-umbrella/pull/48

6. [Python] Bad practice to catch everything

   https://github.com/raccoongang/ecommerce/pull/28

6. catching exceptions like IndexOutOfBounds, NPE etc are considered bad practice unless you wrap them and throw as a new exception

    https://github.com/pepperkick/springboot-ems/pull/2

7.  It's also bad practice to merge two Exceptions into one

    https://github.com/Paul-Gerarts/DevShop/pull/8



##### catch Throwable （算是 pokemon-exception catching 的一种吗）

1.  Isn't it a bad practice to catch Throwable ? Something more specific to the
    https://github.com/MovingBlocks/Terasology/pull/3878

2.  Is It a Bad Practice to Catch Throwable
    https://github.com/eugenp/tutorials/pull/8176

3.  Do not catch Throwable (有原因，会捕获一些无法处理的错误, 如 OutOfMemoryError)

    https://github.com/openhab/openhab-addons/pull/3144

4.  catching throwables is a bad practice

    https://github.com/AppliedEnergistics/Applied-Energistics-2/pull/222

5.  Catching Throwable is bad practice

    https://github.com/jenkinsci/ssh-steps-plugin/pull/23/files?file-filters%5B%5D=.java#r291995312

6.  

##### except: pass

1.  [Python] If you there is an exception, then do something with it.doing just \"pass\" will cause bugs to disappear

    https://github.com/osherdp/python-training/pull/103

2.  [Python] "Except: pass" is a bad programming practice.

    https://github.com/scikit-learn/scikit-learn/pull/15839

3.  Empty catch blocks are bad practice and make debugging difficult

    https://github.com/fabric8io/fabric8-maven-plugin/pull/1758

    https://github.com/dev-gaur/fabric8-maven-plugin/commit/b0e984939127f22c220c6cea6ab8cdebcd34c83b#diff-175479c2d7da97c2b7366241b3d2bfad

4.  

#### shadow name

[checkstyle](https://checkstyle.sourceforge.io/apidocs/com/puppycrawl/tools/checkstyle/checks/coding/HiddenFieldCheck.html)

1.  [Python] bad practice to have two variables with the same name, even if the scope of one is more local than the other

    https://github.com/TabbycatDebate/tabbycat/pull/1426

2.  [Python] improper name that overshadows the built-in

    https://api.github.com/repos/AfricasVoices/RapidProTools/issues/79

3.  [Python] While `type` is technically not a reserved keyword, it is bad practice to shadow builtin function names e.g. `type()`

    https://github.com/DataDog/integrations-core/pull/5264

4.  this local local object was hiding the global object (Sonar)  

    https://github.com/openmrs/openmrs-core/pull/3072

5.  [Python] It's a bad practice to overwrite existing built-in names.

    https://github.com/reponche/Weatherbot-2.0/pull/18

6. Refactored Object name to uncover global version

   https://github.com/openmrs/openmrs-core/pull/3072

7. 

#### mutable object as default value

1.  [Python] used `{}` (mutable object) as a default argument (有原因)

    https://github.com/NeKitDS/gd.py/pull/12

2.  [Python] Definitely bad practice to use mutable types in method signatures. You can do e.g. `other_values = other_values or {}` in the body instead.  (后面是说 `{}` 可以吗？)

    https://github.com/galaxyproject/galaxy/pull/1861

3.  Exposing internal representations of mutable objects in getters and setters (FindBugs or Sonar若 setters 传入的参数是mutable的，则赋值时应重新 new 一个，而不是直接赋值为传进来的 object ;  若 getters 返回的参数是 mutable 的，则应该返回一个 clone 版本，而不是原变量 )

    https://github.com/openmrs/openmrs-core/pull/3094

4.  [Python] bad practice to use a mutable as default value 

    https://github.com/c4urself/bump2version/pull/47

5. [Python] Using a mutable list as a default arg creates a global

   https://github.com/nilp0inter/cpe/pull/32/files

6. [Python] using a read-write parameter as a default

    https://github.com/SpiNNakerManchester/sPyNNaker/pull/666

7. 

#### tests 相关

1.  Using thread.sleep in android tests is a bad practice
    https://github.com/Zeavee/Run0rD1e/pull/145

2.  bad practice to have explicit System.out calls in tests
    https://github.com/apache/maven-dependency-plugin/pull/41

3.  bad practice to write conditions in tests. so possibly we need a few tests instead of one. test should not have logic (之前还出现过一次，但是没说原因，就没有记录)

    https://github.com/jdi-testing/jdi-light/pull/887

4.  [Python] code lines after assertion, in case assertion fails, never get to those line

    https://github.com/cloudinary/pycloudinary/pull/208

5.  

---

#### SpotBugs Rules

1.  [REC: Exception is caught when Exception is not thrown (REC_CATCH_EXCEPTION)](https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html#rec-exception-is-caught-when-exception-is-not-thrown-rec-catch-exception)

    一个 catch 同时捕获多种 exceptions ; 

    不指明具体种类 exceptions，错误捕获 RuntimeException，从而掩盖错误

    **能检测 catch throwable 吗？**

    >   Exception is not thrown within the try block, and RuntimeException is not explicitly caught.
    >
    >   It is a common bug pattern to say try { ... } catch (Exception e) { something } as a shorthand for **catching a number of types of exception each of whose catch blocks is identical**, but this construct also **accidentally catches RuntimeException** as well, **masking potential bugs**.

2.  [EI: May expose internal representation by returning reference to mutable object (EI_EXPOSE_REP)](https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html#ei-may-expose-internal-representation-by-returning-reference-to-mutable-object-ei-expose-rep)

    >   Returning a reference to a mutable object value stored in one of the object's fields exposes the internal representation of the object. If instances are accessed by untrusted code, and unchecked changes to the mutable object would compromise security or other important properties, you will need to do something different. Returning a new copy of the object is better approach in many situations.

    [EI2: May expose internal representation by incorporating reference to mutable object (EI_EXPOSE_REP2)](https://spotbugs.readthedocs.io/en/stable/bugDescriptions.html#ei2-may-expose-internal-representation-by-incorporating-reference-to-mutable-object-ei-expose-rep2)

    >   This code stores a reference to an externally mutable object into the internal representation of the object. If instances are accessed by untrusted code, and unchecked changes to the mutable object would compromise security or other important properties, you will need to do something different. Storing a copy of the object is better approach in many situations.



#### global variable (Python)

出现很多次了，一开始没有记录. 使用 global 常常意味着应该 rewrite

[why-are-global-variables-evil](https://stackoverflow.com/questions/19158339/why-are-global-variables-evil)

1.  `global actions` the way it is used here is bad practice

    https://github.com/UWPCE-PythonCert-ClassRepos/SP_Online_PY210/pull/714

2. using global is most of the time bad practice

#### printStackTrace()

[Reason-cn](https://www.codenong.com/7469316/)

[Reason-en](https://stackoverflow.com/questions/7469316/why-is-exception-printstacktrace-considered-bad-practice)

1.  exception.printStackTrace() considered bad practice (在特定条件下valid)

    https://github.com/nerisa/java_training/pull/1

2.  e.printStackTrace() is a bad practice 

    https://github.com/apache/geode/pull/4682/files/d8924a8105294286fc38cb6f2a8e602df512382e#diff-6058766d7fc012a3ab7c7729cb108e05R44

3.  

-----------

### Code change 限定

#### import *

1.  wildcard imports are bad practice 

    https://github.com/RiiConnect24-Bot/RC24-Bot/pull/92

2. Avoid to import star which is a bad code practice

   https://github.com/apache/calcite/pull/1910

3. using glob import was considered a bad practice

   https://github.com/thewca/tnoodle-lib/pull/5

4. 

#### catch exception then do nothing

2.  [Python] Catching everything and then passing is very bad practice

     https://github.com/ModOrganizer2/modorganizer-umbrella/pull/48

#### Return Type

1.  Method with Boolean return type returns explicit null

    https://github.com/apache/fineract/pull/696


#### try-catch in control flow block

1.   It is bad practice to use try/catch inside if/else block. Better to create method that will be called inside if block
    https://github.com/E-Kel/Demo3ToDoApp/pull/7

2.  Program flow should never be controlled by exceptions handling

    https://github.com/AY1920S1-CS2113-T13-3/main/pull/55


#### catch throwable

1.  Don’t Catch Throwable 

    https://github.com/apache/hadoop/pull/1923/files?file-filters%5B%5D=.java#diff-da24fd0a9727e2ca3d21c2153fe876baR77

2.  

#### Conditional import [Python]

1.  [python] Conditional import

    https://github.com/apache/libcloud/pull/1387

####  **kwargs [Python]

1.  Using `**kwargs` is a bad practice

    https://github.com/apache/libcloud/pull/1387