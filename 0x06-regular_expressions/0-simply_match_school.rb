def match_school(input)
    # This regex matches 'School' as a whole word, ignoring case
    regex = /\bSchool\b/i
    matches = input.scan(regex)
    matches.each { |match| puts match }
  end
  
  # Example usage:
  input_strings = [
    "Holberton",
    "holberton",
    "H0lberton",
    "aaahHolberton",
    "Holbertonaaa",
    "School",
    "Best School",
    "School Best School",
    "Grace Hopper"
  ]
  
  input_strings.each do |input|
    match_school(input)
  end
  