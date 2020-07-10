def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for weight in range(len(weights)):
        remaining = limit - weights[weight]
        if remaining in cache:
            if weight > cache[remaining]:
                print(f"({weight}, {cache[remaining]})")
                return (weight, cache[remaining])
            else:
                print(f"({cache[remaining]}, {weight})")
                return (cache[remaining], weight)

        cache[weights[weight]] = weight


    return None
