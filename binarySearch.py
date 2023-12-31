def binarySearch(aray, target):
    left, right = 0, len(aray) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the target is at the middle
        if aray[mid] == target:
            return 'Item is present in array'
        
        # If the target is greater, ignore left half
        elif aray[mid] < target:
            left = mid + 1
        
        # If the target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target is not in the array
    return 'Item not present in the list'

#Allows user to create their own array and then prints it out afterwards
aray = []
item = 'placeholder'
while item != '':
    item = input('Enter an item name to be added to the array (leave blank to finish): ')
    if item != '':
         aray.append(item)

print(f'\n{aray}')

target = input('Enter item to be searched for: ')

print(binarySearch(aray,target))


