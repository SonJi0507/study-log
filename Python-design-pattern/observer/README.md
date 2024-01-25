# 파이썬에서의 옵저버 패턴 예제

이것은 파이썬에서 구현된 옵저버(Observer) 디자인 패턴의 예제입니다. 옵저버 패턴은 객체 간의 일대다 관계를 설정하여 한 객체의 상태가 변경되면 해당 객체에 의존하는 모든 객체가 자동으로 알림을 받고 업데이트되는 디자인 패턴입니다. 이 예제에서는 `NewsPublisher` 클래스가 주체(Subject) 역할을 하고 `SMSSubscriber`, `EmailSubscriber`, `AnyOtherSubscriber`와 같은 여러 구독자 클래스가 관찰자(Observer)로 동작합니다.

## 구현

### NewsPublisher 클래스

- `NewsPublisher` 클래스는 이 예제에서 주체(Subject) 역할을 합니다.
- 이 클래스는 구독자 목록, 최신 뉴스 및 구독자를 관리하고 알림을 보내는 메서드를 제공합니다.
- `attach(subscriber)`: 구독자를 목록에 추가합니다.
- `detach()`: 가장 최근에 추가된 구독자를 제거합니다.
- `subscribers()`: 구독자 유형의 목록을 반환합니다.
- `notifySubscribers()`: 모든 구독자에게 `update()` 메서드를 호출하여 알림을 보냅니다.
- `addNews(news)`: 최신 뉴스를 설정합니다.
- `getNews()`: 최신 뉴스를 가져옵니다.

### Subscriber 추상 클래스

- `Subscriber` 추상 클래스는 구체적인 구독자가 구현해야 하는 인터페이스를 정의합니다.

### 구체적인 구독자 클래스 (`SMSSubscriber`, `EmailSubscriber`, `AnyOtherSubscriber`)

- 이러한 클래스는 구체적인 관찰자(Observer) 역할을 합니다.
- 뉴스 게시자(`NewsPublisher`)에서 뉴스 업데이트를 받습니다.
- `update()` 메서드를 구현하여 뉴스 업데이트에 대한 반응 방식을 정의합니다.

## 사용법

```python
if __name__ == "__main__":
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("\n구독자 목록:", news_publisher.subscribers())

    news_publisher.addNews("안녕, 세계!")
    news_publisher.notifySubscribers()

    print("\n구독자 분리:", type(news_publisher.detach()).__name__)
    print("\n구독자 목록:", news_publisher.subscribers())

    news_publisher.addNews("내 두 번째 뉴스!")
    news_publisher.notifySubscribers()
```

## 작동 방식
1. NewsPublisher 객체를 생성합니다.
2. 구독자 클래스(SMSSubscriber, EmailSubscriber, AnyOtherSubscriber)의 인스턴스를 생성하고 이를 게시자에 등록합니다.
3. addNews()를 사용하여 뉴스를 추가하고 notifySubscribers()를 호출하여 구독자에게 알립니다.
4. detach()를 사용하여 구독자를 분리합니다.
5. 더 많은 뉴스를 추가하고 구독자에게 다시 알림을 보냅니다.

이 예제는 옵저버 패턴을 통해 뉴스 게시자와 구독자 사이에 느슨한 결합을 유지하고 게시자의 상태가 변경될 때 자동 업데이트를 가능하게 하는 방법을 보여줍니다. 이 예제를 참고하여 프로젝트에서 옵저버 패턴을 구현하는 데 활용하실 수 있습니다.