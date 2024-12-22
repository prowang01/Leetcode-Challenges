# Solution 1: Value-Shifting

## Idea
Instead of removing a wagon, we **shift the numbers written on the wagons** so that the wagon we want to remove is "erased". Afterward, we simply remove the first wagon as it no longer has a place.

---

### Example: `1 → 2 → 3 → 4 → 5`, \(n = 2\)
We need to remove the **2nd wagon from the end** (the wagon with `4`).

#### Step 1: Count wagons from the back.
- Imagine you are at the back of the train.
- You move toward the front (from `5` to `1`) and record the order:
  - `5` → position 1 from the end.
  - `4` → position 2 from the end.
  - `3` → position 3 from the end.
  - `2` → position 4 from the end.
  - `1` → position 5 from the end.

---

#### Step 2: Shift the numbers.
- When you reach the wagon in **position 3** (`3`), copy its number (`3`) to the next wagon (`4`).  
  Now, wagon `4` becomes `3`.

- When you reach the wagon in **position 2** (`4`), copy its number (`4`) to the next wagon (`5`).  
  Now, wagon `5` becomes `4`.

---

#### Step 3: Remove the first wagon.
- The first wagon no longer has a valid place. Remove it.  
  The train becomes: `1 → 2 → 3 → 4`.

---

### Result
The wagon with the number `4` has disappeared, but the other wagons were just renamed.

---

## Complexity of Value-Shifting
- **Time Complexity**: \(O(n)\)
  - Counting wagons from the back requires \(O(n)\).
  - Shifting the numbers also takes \(O(n)\).
  - Combined, the time complexity is \(O(n)\).
- **Space Complexity**: \(O(n)\) due to the recursive stack, as the recursion depth equals the length of the list.

---

# Solution 2: Index and Remove

## Idea
Instead of shifting numbers, this method **directly removes the wagon** by keeping track of its position and skipping it.

---

### Example: `1 → 2 → 3 → 4 → 5`, \(n = 2\)
We need to remove the **2nd wagon from the end** (the wagon with `4`).

#### Step 1: Count wagons from the back.
- Imagine you are at the back of the train. As in the first solution, you move forward:
  - `5` → position 1 from the end.
  - `4` → position 2 from the end.
  - `3` → position 3 from the end.
  - `2` → position 4 from the end.
  - `1` → position 5 from the end.

---

#### Step 2: Detach the wagon.
- When you reach the wagon in **position 2**, you detach this wagon (`4`).  
  To do this, you tell the previous wagon (`3`) to skip this one and connect directly to the next wagon (`5`).

---

### Result
The train becomes: `1 → 2 → 3 → 5`.  
The wagon `4` has been removed without changing the other wagons.

---

## Complexity of Index and Remove
- **Time Complexity**: \(O(n)\)
  - Counting wagons from the back requires \(O(n)\).
  - Removing the wagon takes \(O(1)\) during the recursion unwind.
  - Combined, the time complexity is \(O(n)\).
- **Space Complexity**: \(O(n)\) due to the recursive stack, as the recursion depth equals the length of the list.

---

# Simplified Comparison

| **Solution**       | **What happens**                                      | **Time Complexity** | **Space Complexity** |
|---------------------|-------------------------------------------------------|----------------------|-----------------------|
| **Value-Shifting**  | Change the numbers on the wagons to "erase" one.      | \(O(n)\)             | \(O(n)\)              |
| **Index and Remove**| Directly detach the wagon from the train.             | \(O(n)\)             | \(O(n)\)              |
