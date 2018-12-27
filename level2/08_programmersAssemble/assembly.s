.global main

main:
    mov $XXXXXXX, %eax
    mov $0, sum
    mov $0x8, constA
loop:
    test %eax, %eax
    jz fin
    add constA, sum
    dec %eax
    jmp loop
fin:
    cmp $0xb790, sum
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
