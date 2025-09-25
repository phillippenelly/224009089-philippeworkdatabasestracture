# Stack Implementation for MoMo Pay Transaction Steps
def momo_pay_stack():
    """
    Simulates MoMo Pay transaction stack where steps are pushed and popped (undone)
    """
    # Initialize empty stack for MoMo Pay transaction steps
    momo_stack = []
    
    # Push transaction steps onto the stack in sequence
    momo_stack.append("Select Service")  # First step
    momo_stack.append("Enter Amount")    # Second step
    momo_stack.append("Confirm")         # Third step (last step)
    
    print("MoMo Pay Transaction Stack:")
    print("Initial steps:", momo_stack)
    print(f"Current step: {momo_stack[-1]}")
    print()
    
    # Pop one step (undo last action)
    undone_step = momo_stack.pop()
    print(f"Undone step: {undone_step}")
    print("Remaining steps:", momo_stack)
    
    if momo_stack:
        print(f"Step left: {momo_stack[-1]}")
        return momo_stack[-1]
    else:
        print("All steps completed/undone!")
        return None

# Execute MoMo Pay simulation
print("=" * 60)
print("MOCO PAY TRANSACTION STACK SIMULATION")
print("=" * 60)
momo_result = momo_pay_stack()
print("=" * 60)

# Stack Implementation for UR Student Notes
def ur_notes_stack():
    """
    Simulates UR student notes stack with multiple pop operations
    """
    # Initialize stack for student notes
    notes_stack = []
    
    # Push notes onto the stack (most recent note on top)
    notes_stack.append("Note1")  # First note
    notes_stack.append("Note2")  # Second note
    notes_stack.append("Note3")  # Third note (most recent)
    
    print("UR Student Notes Stack:")
    print("Initial notes:", notes_stack)
    print(f"Top note: {notes_stack[-1]}")
    print()
    
    # Pop twice (remove two most recent notes)
    first_pop = notes_stack.pop()
    second_pop = notes_stack.pop()
    
    print(f"First pop: {first_pop}")
    print(f"Second pop: {second_pop}")
    print("Notes remaining:", notes_stack)
    
    if notes_stack:
        print(f"Note left: {notes_stack[-1]}")
        return notes_stack[-1]
    else:
        print("No notes left!")
        return None

# Execute UR Notes simulation
print("\n" + "=" * 60)
print("UR STUDENT NOTES STACK SIMULATION")
print("=" * 60)
notes_result = ur_notes_stack()
print("=" * 60)

# Challenge: Complex Stack Operations with Push and Pop
def stack_operations_challenge():
    """
    Challenge: Push A,B,C, pop once, then push D, and show final top
    """
    # Initialize empty stack
    stack = []
    
    print("CHALLENGE: Complex Stack Operations")
    print("=" * 40)
    
    # Algorithm Step 1: Push initial elements A, B, C
    print("Step 1: Push A, B, C")
    stack.append("A")  # Push A
    stack.append("B")  # Push B
    stack.append("C")  # Push C
    print(f"Stack after pushes: {stack}")
    print(f"Current top: {stack[-1]}")
    print()
    
    # Algorithm Step 2: Pop once (remove top element)
    print("Step 2: Pop once")
    popped = stack.pop()
    print(f"Popped element: {popped}")
    print(f"Stack after pop: {stack}")
    print(f"Current top: {stack[-1]}")
    print()
    
    # Algorithm Step 3: Push new element D
    print("Step 3: Push D")
    stack.append("D")  # Push D
    print(f"Stack after pushing D: {stack}")
    print(f"Final top: {stack[-1]}")
    print()
    
    # Algorithm Step 4: Display final result
    print("FINAL RESULT:")
    print(f"Stack: {stack}")
    print(f"Top element: {stack[-1]}")
    
    return stack[-1]

# Execute challenge
print("\n" + "=" * 60)
print("STACK OPERATIONS CHALLENGE")
print("=" * 60)
challenge_result = stack_operations_challenge()
print("=" * 60)

# Queue Implementation for RRA Office Service
def rra_citizen_queue():
    """
    Simulates citizen queue at RRA office with FIFO service
    """
    from collections import deque
    
    # Initialize queue for citizens
    citizen_queue = deque()
    
    # Add 8 citizens to the queue
    for i in range(1, 9):
        citizen_queue.append(f"Citizen{i}")
    
    print("RRA Office Citizen Queue:")
    print("Initial queue:", list(citizen_queue))
    print(f"Total citizens: {len(citizen_queue)}")
    print(f"First in line: {citizen_queue[0]}")
    print()
    
    # Serve 4 citizens (dequeue 4 times)
    print("Serving 4 citizens...")
    for i in range(4):
        served_citizen = citizen_queue.popleft()
        print(f"Served: {served_citizen}")
    
    print("\nQueue after serving 4 citizens:")
    print("Remaining queue:", list(citizen_queue))
    
    if citizen_queue:
        print(f"Now in front: {citizen_queue[0]}")
        return citizen_queue[0]
    else:
        print("Queue is empty!")
        return None

# Execute RRA queue simulation
print("\n" + "=" * 60)
print("RRA OFFICE CITIZEN QUEUE SIMULATION")
print("=" * 60)
rra_result = rra_citizen_queue()
print("=" * 60)

# Queue Implementation for Nyabugogo Bus Departure
def nyabugogo_bus_queue():
    """
    Simulates bus queue at Nyabugogo taxi park
    """
    from collections import deque
    
    # Initialize queue for buses
    bus_queue = deque()
    
    # Add 5 buses to the queue
    buses = ["Bus1 (Kigali)", "Bus2 (Musanze)", "Bus3 (Rubavu)", "Bus4 (Huye)", "Bus5 (Rusizi)"]
    for bus in buses:
        bus_queue.append(bus)
    
    print("Nyabugogo Bus Queue:")
    print("Buses in queue:", list(bus_queue))
    print(f"Total buses waiting: {len(bus_queue)}")
    print()
    
    # Show which bus departs first
    first_bus = bus_queue[0]
    print(f"Next bus to depart: {first_bus}")
    print("(Buses depart in FIFO order - first in, first out)")
    
    return first_bus

# Execute Nyabugogo simulation
print("\n" + "=" * 60)
print("NYABUGOGO BUS QUEUE SIMULATION")
print("=" * 60)
bus_result = nyabugogo_bus_queue()
print("=" * 60)

# Challenge: Priority Queue for CHUK Emergency Department
def chuk_emergency_priority_queue():
    """
    Implements priority queue for CHUK emergency cases
    """
    import heapq
    
    # Initialize priority queue (min-heap)
    emergency_queue = []
    
    print("CHUK EMERGENCY PRIORITY QUEUE SYSTEM")
    print("=" * 50)
    print("Priority Levels: 1-Critical, 2-Emergent, 3-Urgent, 4-Routine")
    print()
    
    # Algorithm Step 1: Add emergency cases with priorities
    print("Step 1: Adding emergency cases with priorities")
    
    # Priority format: (priority_level, timestamp, patient_description)
    heapq.heappush(emergency_queue, (2, "08:00", "PatientA - Fracture"))      # Emergent
    heapq.heappush(emergency_queue, (1, "08:05", "PatientB - Cardiac Arrest")) # Critical
    heapq.heappush(emergency_queue, (4, "08:10", "PatientC - Routine Check"))  # Routine
    heapq.heappush(emergency_queue, (1, "08:15", "PatientD - Severe Bleeding"))# Critical
    heapq.heappush(emergency_queue, (3, "08:20", "PatientE - High Fever"))     # Urgent
    
    print("Emergency cases added to queue")
    print()
    
    # Algorithm Step 2: Process cases in priority order
    print("Step 2: Processing cases by priority order")
    print("Treating patients in order of medical urgency:")
    print()
    
    case_number = 1
    while emergency_queue:
        priority, time, patient = heapq.heappop(emergency_queue)
        priority_text = {1: "CRITICAL", 2: "EMERGENT", 3: "URGENT", 4: "ROUTINE"}[priority]
        print(f"Case {case_number}: {priority_text} - {patient} (Arrived: {time})")
        case_number += 1
    
    print()
    
    # Algorithm Step 3: Comparison with simple queue
    print("Step 3: Why Priority Queue is better than Simple Queue")
    print("✓ Medical urgency prioritized over arrival time")
    print("✓ Critical cases treated immediately (saves lives)")
    print("✓ Better resource allocation in emergency department")
    print("✓ Reduces mortality rates for serious conditions")
    print("✗ Simple FIFO queue would treat routine cases before emergencies")
    
    return "Priority Queue is essential for medical emergencies"

# Execute CHUK emergency simulation
print("\n" + "=" * 60)
print("CHUK EMERGENCY PRIORITY QUEUE CHALLENGE")
print("=" * 60)
emergency_result = chuk_emergency_priority_queue()
print("=" * 60)