#!/bin/bash

# Ask the user for their age
echo "Please enter your age:"
read age

# Check if the age is a valid number
if ! [[ "$age" =~ ^[0-9]+$ ]]; then
    echo "Please enter a valid number for age."
    exit 1
fi

# Conditional statements to classify the user based on age
if [ $age -lt 18 ]; then
    echo "You are a minor."
elif [ $age -ge 18 ] && [ $age -lt 65 ]; then
    echo "You are an adult."
else
    echo "You are a senior."
fi

