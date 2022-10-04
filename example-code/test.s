	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 1
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movl	$0, -4(%rbp)
	movl	$2, -8(%rbp)
	movl	$3, -12(%rbp)
	movl	-8(%rbp), %eax
	movl	%eax, %ecx
	addl	$-1, %ecx
	movl	%ecx, -8(%rbp)
	cmpl	-12(%rbp), %eax
	jge	LBB0_2
## %bb.1:
	movl	-8(%rbp), %eax
	movl	%eax, %ecx
	addl	$-1, %ecx
	movl	%ecx, -8(%rbp)
	movl	%eax, -20(%rbp)                 ## 4-byte Spill
	jmp	LBB0_3
LBB0_2:
	movl	-12(%rbp), %eax
	movl	%eax, -20(%rbp)                 ## 4-byte Spill
LBB0_3:
	movl	-20(%rbp), %eax                 ## 4-byte Reload
	movl	%eax, -16(%rbp)
	movl	-8(%rbp), %esi
	movl	-12(%rbp), %edx
	movl	-16(%rbp), %ecx
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	-4(%rbp), %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%d %d %d\n"

.subsections_via_symbols
