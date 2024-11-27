# Behavioral Design Patterns

**Author:** Ernu Catalina FAF-223

## Objectives

1. Study and understand the Behavioral Design Patterns.  
2. As a continuation of the previous laboratory work, analyze the communication between software entities in the bookstore system.  
3. Implement additional functionalities using behavioral design patterns to improve communication and adaptability.  

## Used Behavioral Design Patterns

- **Iterator Pattern**: Provides sequential access to items in a collection, like books in a bundle, without exposing the underlying structure.  

- **Strategy Pattern**: Allows dynamic selection and application of pricing strategies, enabling flexible price adjustments for discounts or markups.  

- **Observer Pattern**: Facilitates automatic notifications to customers about changes in order status or new promotions, enhancing engagement.  

## Implementation

### Iterator Pattern  
- **Explanation:**  
  The `BundleIterator` class is introduced to traverse a `BookBundle`. It provides an interface to iterate through items while hiding the internal details of the collection.  

- **Example Scenario:**  
  A customer wants to browse through all books in a bundle they have ordered. The `BundleIterator` allows easy traversal:  
  ```python
  bundle_iterator = BundleIterator(bundle)
  for item in bundle_iterator:
      print(item.get_info())
  ```

### Strategy Pattern  
- **Explanation:**  
  The `PricingStrategy` interface defines a flexible pricing mechanism. Specific strategies, such as `WeekendDiscountStrategy` and `HolidayMarkupStrategy`, adjust order prices dynamically based on business needs.  

- **Example Scenario:**  
  The bookstore applies a 20% discount during weekends. The Strategy pattern enables dynamic selection and application of this pricing logic:  
  ```python
  pricing_context = PricingContext(WeekendDiscountStrategy())
  final_price = pricing_context.get_price(order)
  ```

### Observer Pattern  
- **Explanation:**  
  The `OrderNotifier` subject allows customers to subscribe for updates. Whenever the order status changes or a new promotion is launched, all subscribed customers (observers) are notified automatically.  

- **Example Scenario:**  
  A customer receives an email notification when their order is shipped:  
  ```python
  notifier.add_observer(customer)
  notifier.notify("Your order has been shipped!")
  ```

## Execution  

1. **Browse Bundles:**  
   Customers can use the Iterator pattern to explore books in an ordered bundle effortlessly.  

2. **Dynamic Pricing:**  
   The Strategy pattern provides flexibility in applying discounts or markups based on the store’s business logic.  

3. **Customer Engagement:**  
   The Observer pattern keeps customers informed about their order status and promotions, improving their overall experience.  

## Conclusions  

In this project, three behavioral design patterns were implemented to improve communication and adaptability within the bookstore system. The **Iterator Pattern** enabled efficient traversal of book bundles, the **Strategy Pattern** provided a dynamic approach to pricing, and the **Observer Pattern** ensured seamless communication with customers. These patterns enhanced the system's maintainability and user experience, showcasing the effectiveness of behavioral design patterns in software design.  