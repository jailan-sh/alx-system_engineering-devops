#!/usr/bin/env ruby
#non-capturing method
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\] /).join(',')

#lookbehind
#print ARGV[0].scan(/(?<=from:)[+0-9a-zA-Z]+/).join
#print (',')
#print ARGV[0].scan(/(?<=to:)[+0-9a-zA-Z]+/).join
#print (',')
#puts ARGV[0].scan(/(?<=flags:)[-:0-9]+/).join
