#### Introduction

; Set up some registers (sorta like variables) with values
; In the debugger, look how these change!
mov rax, 0
mov rbx, 1
mov rcx, 2
mov rdx, 3
mov rsi, 4
mov rdi, 5
mov rbp, 6

; Push and pop - watch how the stack changes!
push 0x12345678
pop rax

push 0x1111
push 0x2222
push 0x3333
pop rax
pop rax
pop rax

; This creates a string and references it in rax - watch the debugger!
call getstring
  db "Hello World!",0
getstring:
pop rax

; Finally, return 0x1337
mov rax, 0x1337
ret


##### Loops

; We want to loop 5 times - you can change this if you want!
mov rax, 3

; Top of the loop
top:
  ; Decrement rax
  dec rax

  ; Jump back to the top until rax is zero
  jnz top

; Cleanly return after the loop
ret

##### Getting Started

; This is a comment! We'll use comments to help guide your journey.
; Right now, we just need to RETurn!
;
; Enter a return statement below and hit Execute to see what happens!
ret

##### Returning a Value

; TODO: Set rax to 1337
mov rax, 1337

; Return, just like we did last time
ret

##### System Calls

; TODO: Find the syscall number for sys_exit and put it in rax
mov rax, 3Ch
; TODO: Put the exit_code we want (99) in rdi
mov rdi, 99
; Perform the actual syscall
syscall


##### Calling into the Void

; Push this value to the stack
push 0x12345678

; Try to return
ret


##### Getting RIP

; Remember, this call pushes the return address to the stack
call place_below_the_nop

; This is where the function *thinks* it is supposed to return
nop

; This is a 'label' - as far as the call knows, this is the start of a function
place_below_the_nop:

; TODO: Pop the top of the stack into rax
pop rax

; Return from our code, as in previous levels
ret

##### Hello World!

; This would be a good place for a call
call place_below_the_nop

; This is the literal string 'Hello World', null terminated, as code. Except
; it'll crash if it actually tries to run, so we'd better jump over it!
db 'Hello World',0

; This would be a good place for a label and a pop
place_below_the_nop:
pop rax

; This would be a good place for a re... oh wait, it's already here. Hooray!
ret


##### Hello World

; TODO: Get a reference to this string into the correct register
call amirootyet
db 'Hello World!',0

amirootyet:
; Set up a call to sys_write
mov rax, 1

; TODO: Set rdi to the first argument (the file descriptor, 1)
mov rdi, 1

; TODO: Set rsi to the second argument (buf - this is the "Hello World" string)
pop rsi

; TODO: Set rdx to the third argument (length of the string, in bytes)
mov rdx, 12

; Perform the syscall
syscall

; Return cleanly
ret

##### Opening a File

; TODO: Get a reference to this string into the correct register
call amirootyet
db '/etc/passwd',0

amirootyet:
; Set up a call to sys_open
; TODO: Set rax to the correct syscall number
mov rax, 2

; TODO: Set rdi to the first argument (the filename)
pop rdi

; TODO: Set rsi to the second argument (flags - 0 is fine)
mov rsi, 0

; TODO: Set rdx to the third argument (mode - 0 is also fine)
mov rdx, 0

; Perform the syscall
syscall

; syscall sets rax to the file handle, so to return the file handle we don't
; need to do anything else!
ret

##### Reading a File

; TODO: Get a reference to this
; TODO: Get a reference to this
call amirootyet
db '/var/northpolesecrets.txt',0

amirootyet:
; TODO: Call sys_open
mov rax, 2
pop rdi
mov rsi, 0
mov rdx, 0
syscall

; TODO: Call sys_read on the file handle and read it into rsp
 push rdi  
 push rax 
 mov rax, 0 
 pop rdi 
 pop rsi
 mov rdx, 70
 syscall

; TODO: Call sys_write to write the contents from rsp to stdout (1)
 mov rax, 1 
 mov rdi, 1 
 mov rdx, 70
 syscall 
 ret

; TODO: Call sys_exit
mov rax, 60
mov rdi, 1