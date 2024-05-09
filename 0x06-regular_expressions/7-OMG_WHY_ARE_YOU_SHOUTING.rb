#!/usr/bin/env ruby
# A michael regular expression that is matches only capital letters
puts ARGV[0].scan(/[A-Z]/).join
