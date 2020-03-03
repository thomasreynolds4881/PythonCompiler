multiply_long
				STMFD	sp!, {r2,r3,r4,r5} ; protect some register on stack
				MOV	r2, #0					; upper half of multiplicand
				MOV	r3, #0					; lower half of product
				MOV	r4, #0					; upper half of product
				MOV	r5, #32					; loop counter
mul_lp			TST		r1, #1		; check right bit of multiplier
				BEQ	mul1					; conditionally
				ADDS	r3, r3, r0		;    add 64-bit multiplicand
				ADC	r4, r4, r2	 		;    to 64-bit product
mul1			LSL		r2, r2, #1		; shift 64-bit multiplicand left one bit,
				LSLS	r0, r0, #1			;    shifting high half first and maybe
				BCC	mul2					;    adjusting it after shifting low half
				ORR	r2, r2, #1			;    so as not to lose transfered bit
mul2			LSR		r1, r1, #1		; shift multiplier right one bit
				SUBS	r5, r5, #1			; decrement counter
				BNE	mul_lp				; loop 32 times
				MOV	r0, r3					; move product into r1, r0
				MOV	r1, r4					;
				LDMFD	sp!, {r2,r3,r4,r5} ; restore register values from stack
				MOV	pc, lr					; return

divide_long
				STMFD	sp!, {r3,r4,r5}	; protect some register values on stack
				MOV		r3, #0		; r2,r3 is 64-bit shifted divisor
				MOV		r4, #0		; initialize quotient to zero
				MOV		r5, #33		; loop counter
div_lp			SUBS	r0, r0, r3	; subtract shifted divisor from dividend
				SBCS	r1, r1, r2	;
				BCS		div1		;
				ADDS	r0, r0, r3	; add it back if we went negative
				ADC		r1, r1, r2	;
				LSL		r4, r4, #1	; shift quotient left one bit
				B		div2		;
div1			LSL		r4, r4, #1	; shift quotient left one bit, but also
				ORR		r4, r4, #1	;    set least significant bit to 1
div2			LSRS	r2, r2, #1	; shift shifted divisor right one bit
				RRX		r3, r3		;
				SUBS	r5, r5, #1	; decrement counter
				BNE		div_lp		; loop 33 times (not 32!)
				MOV		r2, r4		; move quotient into r2
				LDMFD	sp!, {r3,r4,r5}	; restore register values from stack
				MOV		pc, lr		; return

signed_multiply
				STMFD	sp!, {r2, lr}	; protect some register values on stack
				MOV		r2, #0			; r2 will remember about negation issue
				CMP		r0, #0			; is r0 negative?
				BGE		sm1				;
				RSB		r0, r0, #0 		; change r0 to its absolute value
				MVN		r2, r2			; bitwise not r2
sm1				CMP		r1, #0			; is r1 negative?
				BGE		sm2				;
				RSB		r1, r1, #0		; change r1 to its absolute value
				MVN		r2, r2			; bitwise not r2
sm2				BL		multiply_long	; multiply absolute values
				TEQ		r2, #0			; need to negate answer?
				BEQ		sm3				;
				RSB		r0, r0, #0		; negate answer
sm3				CMP		r1, #0			; answer too long?
				BEQ		sm4				;
				MOV		r1, #1			;
sm4				LDMFD	sp!, {r2, lr}	; restore register values from stack
				MOV		pc, lr			; return

signed_divide
				STMFD	sp!, {r1, r2, r3, lr} ; protect some register on stack
				MOV		r3, #0			; r3 will remember about negation issue
				CMP		r0, #0			; is r0 negative?
				BGE		sd1             ;
				RSB		r0, r0, #0 		; change r0 to its absolute value
				MVN		r3, r3			; bitwise not r3
sd1				CMP		r1, #0			; is r1 negative?
				BGE		sd2				;
				RSB		r1, r1, #0		; change r1 to its absolute value
				MVN		r3, r3			; bitwise not r3
sd2				MOV		r2, r1			; need divisor in r2 before procedure call
				MOV		r1, #0			;    and also need zero in r1
				BL		divide_long		; multiply absolute values
				MOV		r0, r2			; need quotient in r0 after procedure call
				TEQ		r3, #0			; need to negate answer?
				BEQ		sd3				;
				RSB		r0, r0, #0		; negate answer
sd3				LDMFD	sp!, {r1, r2, r3, lr} ; restore register values from stack
				MOV		pc, lr			; return