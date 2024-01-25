# 심플 팩토리 메서드( Simple Factory Method) 패턴 예제

심플 팩토리 메서드 패턴은 객체 생성을 캡슐화하고, 하위 클래스에서 객체를 생성하는 방법을 결정하도록 하는 디자인 패턴입니다. 이를 통해 객체 생성 과정을 확장하고 클라이언트 코드를 변경하지 않고 새로운 객체를 추가할 수 있습니다.

## 동물과 동물 팩토리

### `Animal` 추상 클래스

- `do_say` 메서드를 추상 메서드로 정의합니다.
- 이를 상속하는 구체적인 동물 클래스들은 `do_say` 메서드를 구현하여 동물의 소리를 출력합니다.

### `Dog`와 `Cat` 클래스

- `Animal`을 상속하는 구체적인 동물 클래스들입니다.
- 각 클래스는 `do_say` 메서드를 구현하여 개와 고양이의 소리를 출력합니다.

### `ForestFactory` 클래스

- `make_sound` 메서드를 정의합니다.
- 이 메서드는 입력된 동물 타입에 따라 해당 동물 객체를 생성하고 소리를 출력합니다.

## 사용법

```python
ff = ForestFactory()
animal = input("어떤 동물 소리를 듣고 싶으세요? [Dog 또는 Cat]")
ff.make_sound(animal)
```

## 작동 방식
1. ForestFactory 객체를 생성합니다.
2. 사용자로부터 어떤 동물 소리를 듣고 싶은지 입력을 받습니다.
3. 입력된 동물 타입에 따라 해당 동물 객체를 생성합니다.
4. do_say 메서드를 호출하여 동물의 소리를 출력합니다.

이 예제에서는 팩토리 메서드 패턴을 사용하여 동물 객체를 생성하고 해당 동물의 소리를 출력하는 방법을 보여줍니다. 이를 통해 새로운 동물을 추가하거나 동물 소리를 변경할 때 클라이언트 코드를 수정하지 않고도 확장이 가능합니다.


---


# 팩토리 메서드(Factory Method) 패턴 예제

팩토리 메서드 패턴은 객체 생성을 캡슐화하여 클라이언트 코드에서 객체의 구체적인 생성 과정을 알 필요가 없도록 하는 디자인 패턴입니다. 이 패턴을 사용하면 객체의 생성 및 초기화가 하위 클래스에 위임되어 확장 가능한 디자인을 구현할 수 있습니다.

## 섹션과 프로필

### `Section` 추상 클래스

- `describe` 메서드를 추상 메서드로 정의합니다.
- 이를 상속하는 구체적인 섹션 클래스들은 `describe` 메서드를 구현하여 섹션의 설명을 출력합니다.

### `PersonalSection`, `AlbumSection`, `PatentSection`, `PublicationSection` 클래스

- `Section`을 상속하는 구체적인 섹션 클래스들입니다.
- 각 클래스는 `describe` 메서드를 구현하여 해당 섹션의 설명을 출력합니다.

### `Profile` 추상 클래스

- 프로필을 생성하는 메서드인 `createProfile`을 추상 메서드로 정의합니다.
- 프로필에 섹션을 추가하는 `addSections` 메서드와 섹션 목록을 반환하는 `getSections` 메서드를 정의합니다.

### `linkedin`, `facebook` 클래스

- `Profile`을 상속하는 구체적인 프로필 클래스입니다.
- `createProfile` 메서드를 구현하여 해당 프로필에 필요한 섹션을 추가합니다.

## 사용법

```python
profile_type = input("어떤 프로필을 생성하시겠습니까? [LinkedIn 또는 FaceBook]")
profile = eval(profile_type.lower())()
print("프로필 생성 중...", type(profile).__name__)
print("프로필에는 다음과 같은 섹션이 있습니다 --", profile.getSections())
```

## 작동 방식
1. 사용자에게 어떤 프로필을 생성할지 입력을 받습니다.
2. 입력에 따라 linkedin 또는 facebook 클래스의 객체를 생성합니다.
3. 해당 프로필 객체의 createProfile 메서드를 호출하여 필요한 섹션을 추가합니다.
4. getSections 메서드를 사용하여 프로필에 추가된 섹션 목록을 확인합니다.

이 예제에서는 팩토리 메서드 패턴을 사용하여 각 프로필 클래스가 자체적으로 섹션을 생성하도록 구현되어 있습니다. 이 패턴을 사용하면 클라이언트 코드는 어떤 프로필을 생성하든 일관된 방식으로 섹션을 추가할 수 있으며, 새로운 프로필 및 섹션을 확장하기가 쉽습니다.


---


# 추상 팩토리(Abstract Factory) 패턴 예제

추상 팩토리 패턴은 객체 생성을 추상화하고, 클라이언트 코드에서 구체적인 객체 생성 로직과 클래스를 분리하는 디자인 패턴입니다. 이 패턴은 관련된 객체 패밀리를 생성하고 변경하기 위한 일관된 인터페이스를 제공합니다. 

## 팩토리와 팩토리 메서드

### `PizzaFactory` 추상 클래스

- `createVegPizza`와 `createNonVegPizza` 메서드를 추상 메서드로 정의합니다.
- 이를 상속하는 구체적인 팩토리 클래스들은 이 메서드들을 구현하여 객체 생성을 담당합니다.

### `IndianPizzaFactory`와 `USPizzaFactory` 클래스

- `PizzaFactory`를 상속하는 구체적인 팩토리 클래스입니다.
- `createVegPizza`와 `createNonVegPizza` 메서드를 구현하여 각각 인도식과 미국식 피자를 생성합니다.

## 피자와 피자 서브클래스

### `VegPizza`와 `NonVegPizza` 추상 클래스

- `prepare`와 `serve` 메서드를 추상 메서드로 정의합니다.
- 이를 상속하는 구체적인 피자 클래스들은 이 메서드들을 구현하여 피자를 준비하고 제공합니다.

### `DeluxVeggiePizza`, `ChickenPizza`, `MexicanVegPizza`, `HamPizza` 클래스

- `VegPizza`와 `NonVegPizza`를 상속하는 구체적인 피자 서브클래스입니다.
- 각 클래스는 피자를 준비하고 제공하는 방식을 구체적으로 구현합니다.

## 피자 스토어

### `PizzaStore` 클래스

- 피자를 만드는 메서드인 `makePizzas`를 구현합니다.
- `PizzaFactory` 객체를 생성하고, 해당 팩토리를 사용하여 피자를 생성하고 준비하고 제공합니다.

## 사용법

```python
pizza = PizzaStore()
pizza.makePizzas()
```

## 작동 방식
1. PizzaStore 객체를 생성합니다.
2. makePizzas 메서드를 호출하여 IndianPizzaFactory와 USPizzaFactory를 사용하여 인도식과 미국식 피자를 생성하고 준비하며 제공합니다.

이 예제에서는 추상 팩토리 패턴을 사용하여 피자 팩토리를 추상화하고, 지역에 따라 다른 스타일의 피자를 생성하고 제공하는 방법을 보여줍니다. 이로써 객체 생성 로직과 사용 로직을 분리하고, 코드의 확장성과 유지보수성을 향상시킬 수 있습니다.