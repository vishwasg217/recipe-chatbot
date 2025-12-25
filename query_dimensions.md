# Query Dimensions

## Dimensions

### Cuisine  

- Type: string
- Optional: Yes
- Values:
Indian, Chinese, Mexican, Italian, American Fast Food, Middle Eastern, English, None

### Meal Type

- Type: string
- Optional: Yes
- Values:
Breakfast, Lunch, Dinner, Snack, Dessert, Drink

### Dietary Restrictions

- Type: list[string]
- Optional: Yes
- Values:
Vegetarian, Gluten-free, Dairy-free, Nut-free, Sugar-free, Low-carb, No Beef, No Seafood, None

### Time Available

- Type: range[integer]
- Optional: Yes
- Values:
10 - 180 minutes

### Ingredient Base

- Type: string
- Optional: Yes
- Values:
Open ended

## Combinations

- (English, Breakfast, Dairy-free, 20-30 minutes, Eggs)
- (Indian, Lunch, None, 30-60 minutes, Mutton)
- (Mexican, Dinner, None, 30-60 minutes, Chicken)
- (Italian, Dessert, None, 15-20 minutes, Chocolate)
- (American Fast Food, Dinner, No Beef, 30-60 minutes, Burger)
- (Middle Eastern, Lunch, No Beef, 30-60 minutes, Lamb)
- (Chinese, Lunch, No Beef No Seafood, 30-60 minutes, Chicken)
- (Indian, Breakfast, Vegetarian, 20-30 minutes, Rice)
- (None, Breakfast, Smoothie, 10-20 minutes, Banana)
- (Italian, Lunch, Vegetarian, 45-60 minutes, Pasta)
- (Chinese, Dinner, Gluten-free, 40-50 minutes, Shrimp)
- (Mexican, Breakfast, Vegetarian, 15-25 minutes, Avocado)
- (Indian, Dinner, Vegetarian Dairy-free, 60-90 minutes, Lentils)
- (None, Snack, Nut-free, 10-15 minutes, Yogurt)
- (American Fast Food, Lunch, None, 20-30 minutes, Fries)
- (Middle Eastern, Dinner, Vegetarian, 50-70 minutes, Chickpeas)
- (English, Lunch, None, 30-45 minutes, Fish)
- (Chinese, Breakfast, Vegetarian, 25-35 minutes, Tofu)
- (Italian, Dinner, Gluten-free Dairy-free, 45-60 minutes, Chicken)
- (Mexican, Snack, Vegetarian, 10-15 minutes, Salsa)
- (Indian, Snack, Vegetarian Gluten-free, 20-30 minutes, Potatoes)
- (None, Dessert, Sugar-free, 15-20 minutes, Berries)
- (American Fast Food, Breakfast, None, 10-15 minutes, Pancakes)
- (Middle Eastern, Breakfast, Vegetarian, 20-30 minutes, Hummus)
- (Chinese, Snack, Vegetarian, 15-20 minutes, Spring Rolls)
- (Italian, Breakfast, None, 10-15 minutes, Coffee)
- (Italian, None, None, None, Chicken)
- (Indian, None, No Beef, None, None)
- (None, Dinner, None, None, None)
- (None, None, Vegetarian, None, lentils)
- (None, Lunch, None, 30 minutes, Rice)
- (Mexican, None, Vegetarian, None, Beans)
- (None, Lunch, None, 20-30 minutes, Salmon)
- (Chinese, Dinner, Low-carb, None, None)

## Queries (from combinations)

- I’m looking for a dairy-free English breakfast with eggs that I can make in about 20–30 minutes.
- Suggest an Indian lunch dish with mutton that takes roughly 30 to 60 minutes to cook.
- What’s a good Mexican chicken dinner that takes under an hour?
- I want a quick Italian dessert with chocolate—something I can make in 15 to 20 minutes.
- Any American fast-food–style burger ideas for dinner, but without beef?
- Looking for a Middle Eastern lamb dish for lunch—no beef, and around an hour of cooking time.
- Can you recommend a Chinese chicken lunch recipe with no beef or seafood?
- I want an Indian vegetarian breakfast using rice that I can finish in about half an hour.
- I need a quick banana smoothie idea for breakfast—something under 20 minutes.
- Suggest an Italian vegetarian pasta for lunch that’s a bit more involved, maybe 45 to 60 minutes.
- Any gluten-free Chinese shrimp dishes that work well for dinner?
- What’s a vegetarian Mexican breakfast that uses avocado and doesn’t take too long?
- I’m planning an Indian vegetarian dinner with lentils—dairy-free, and I don’t mind a longer cook time.
- I want a quick, nut-free yogurt snack I can put together in 10 to 15 minutes.
- Any American fast-food–style lunch ideas with fries that I can make quickly?
- Looking for a Middle Eastern vegetarian dinner using chickpeas, with a cooking time under 70 minutes.
- Suggest an English fish dish for lunch that takes around half an hour.
- What’s a vegetarian Chinese breakfast using tofu that takes about 25 to 35 minutes?
- I want an Italian chicken dinner that’s both gluten-free and dairy-free.
- Need a quick vegetarian Mexican snack—something salsa-based.
- Any Indian vegetarian snacks made with potatoes that are also gluten-free?
- I’m looking for a sugar-free dessert using berries that’s fast to make.
- What’s a quick American-style pancake breakfast I can make in under 15 minutes?
- Suggest a vegetarian Middle Eastern breakfast that includes hummus.
- Any vegetarian Chinese snack ideas like spring rolls that don’t take too long?
- I just want a simple Italian-style breakfast centered around coffee.
- Show me Italian dishes that feature chicken.
- I’m looking for Indian food ideas—just no beef.
- What can I make for dinner tonight?
- Give me some vegetarian ideas using lentils.
- I need a lunch recipe with rice that takes about 30 minutes.
- Any vegetarian Mexican dishes that use beans?
- Suggest a lunch idea with salmon that I can cook in 20–30 minutes.
- I’m looking for low-carb Chinese dinner options.

**Prompt:**

```text
Given the following query combinations, write their natural language forms. 
guidelines: 1. make the query sentences as natural and realistic as possible. 2. do not make them overtly verbose. 3. Try to mirror what a real user would ask interms of sentence structure and tone of voice. 4. make some of them question formed, and some of them sentences. 5. try to change of the sentence structure and when the dimension is mentioned, to add more variety.
```
