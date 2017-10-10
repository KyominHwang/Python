fact:
  addi $sp, $sp -8 # add immediate
  sw $ra, 4($sp) # save word
  sw $a0, 0($sp) # save word
  slti $t0, $a0, 1 # set less than immediate
  beq $t0, $zero, L1 # branch equal
  addi $v0, $zero, 1 # add immediate
  addi $sp, $sp, 8 # add immediate
  jr $ra # jump to returl address

L1:
  addi $a0, $a0, -1 # add immediate
  jal fact # jump Label fact and save next opperator pointer to $ra
  lw $a0, 0($sp) # load word
  lw $ra, 4($sp) # load word
  addi $sp, $sp, 8 # add immediate
  mul $v0, $a0, $v0 #multi
  jr $ra # jump to $ra
