# Set up a variable for the expected payoff
expected_payoff = 0

# Set up a queue to hold the partial histories
q = Queue()

# Initialize the queue with an empty history, with probability 1
q.put((1, '', ''))

while not q.empty():

    # Get an item from the front of the queue
    item = q.get()

    # Set up Strategy objects with the given histories
    player_one = Strategy(item.history1)
    player_two = Strategy(item.history2)

    # Compute the moves that the strategies produce with the given
    # histories, passing the opponent's history as well
    move_one = player_one.next_move(player_two.history)
    move_two = player_two.next_move(player_one.history)

    # Compute the probability of no mistakes occurring
    probability = item.probability * no_mistake_probability * \
                  continuation_probability

    # If this maximum possible term size is larger than the threshold
    if probability * max_payoff > epsilon:
        # Multiply this by the payoff from the outcome of
        # a no-mistake round to find the term
        term = probability * payoff(move_one, move_two)
        # Add the term to the expected payoff
        expected_payoff += term
        # Add the probability along with the histories (including
        # the new moves) back onto the queue
        q.put(probability,
              item.history1 + move_one,
              item.history2 + move_two)

    else:
        # The probability was too small, so don't add it back to
        # the queue

    # Repeat this for each of the two one mistake cases and the
    # two mistake case
