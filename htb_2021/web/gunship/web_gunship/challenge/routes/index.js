0x000055555555a461 <+1>:	push   r15
0x000055555555a463 <+3>:	push   r14
0x000055555555a465 <+5>:	push   r13
0x000055555555a467 <+7>:	push   r12
0x000055555555a469 <+9>:	push   rbx
0x000055555555a46a <+10>:	sub    rsp,0x198
0x000055555555a471 <+17>:	lea    rax,[rip+0x242d60]        # 0x55555579d1d8
0x000055555555a478 <+24>:	mov    QWORD PTR [rsp+0xc8],rax
0x000055555555a480 <+32>:	mov    QWORD PTR [rsp+0xd0],0x1
0x000055555555a48c <+44>:	mov    QWORD PTR [rsp+0xd8],0x0
0x000055555555a498 <+56>:	lea    r13,[rip+0x33989]        # 0x55555558de28
0x000055555555a49f <+63>:	mov    QWORD PTR [rsp+0xe8],r13
0x000055555555a4a7 <+71>:	mov    QWORD PTR [rsp+0xf0],0x0
0x000055555555a4b3 <+83>:	lea    rbx,[rip+0x2076]        # 0x55555555c530 <std::io::stdio::_print>
0x000055555555a4ba <+90>:	lea    rdi,[rsp+0xc8]
0x000055555555a4c2 <+98>:	call   rbx
0x000055555555a4c4 <+100>:	lea    rax,[rip+0x242d1d]        # 0x55555579d1e8
0x000055555555a4cb <+107>:	mov    QWORD PTR [rsp+0xc8],rax
0x000055555555a4d3 <+115>:	mov    QWORD PTR [rsp+0xd0],0x1
0x000055555555a4df <+127>:	mov    QWORD PTR [rsp+0xd8],0x0
0x000055555555a4eb <+139>:	mov    QWORD PTR [rsp+0xe8],r13
0x000055555555a4f3 <+147>:	mov    QWORD PTR [rsp+0xf0],0x0
0x000055555555a4ff <+159>:	lea    rdi,[rsp+0xc8]
0x000055555555a507 <+167>:	call   rbx
0x000055555555a509 <+169>:	mov    QWORD PTR [rsp+0x58],0x1
0x000055555555a512 <+178>:	pxor   xmm0,xmm0
0x000055555555a516 <+182>:	movdqu XMMWORD PTR [rsp+0x60],xmm0
0x000055555555a51c <+188>:	call   QWORD PTR [rip+0x245926]        # 0x55555579fe48
0x000055555555a522 <+194>:	mov    QWORD PTR [rsp+0x90],rax
0x000055555555a52a <+202>:	lea    rdi,[rsp+0xc8]
0x000055555555a532 <+210>:	lea    rsi,[rsp+0x90]
0x000055555555a53a <+218>:	lea    rdx,[rsp+0x58]
0x000055555555a53f <+223>:	call   QWORD PTR [rip+0x245833]        # 0x55555579fd78
0x000055555555a545 <+229>:	cmp    DWORD PTR [rsp+0xc8],0x1
0x000055555555a54d <+237>:	je     0x55555555aa4c <_ZN5rauth4main17h7d7aed61ae7734f4E+1516>
0x000055555555a553 <+243>:	mov    rax,QWORD PTR [rsp+0x90]
0x000055555555a55b <+251>:	lock sub QWORD PTR [rax],0x1
0x000055555555a560 <+256>:	jne    0x55555555a56f <_ZN5rauth4main17h7d7aed61ae7734f4E+271>
0x000055555555a562 <+258>:	lea    rdi,[rsp+0x90]
0x000055555555a56a <+266>:	call   0x55555555ac20 <_ZN5alloc4sync12Arc$LT$T$GT$9drop_slow17h574c4d6eea32be79E>
0x000055555555a56f <+271>:	mov    rax,QWORD PTR [rsp+0x68]
0x000055555555a574 <+276>:	sub    rax,0x1
0x000055555555a578 <+280>:	jb     0x55555555a593 <_ZN5rauth4main17h7d7aed61ae7734f4E+307>
0x000055555555a57a <+282>:	test   rax,rax
0x000055555555a57d <+285>:	je     0x55555555a58e <_ZN5rauth4main17h7d7aed61ae7734f4E+302>
0x000055555555a57f <+287>:	mov    rcx,QWORD PTR [rsp+0x58]
0x000055555555a584 <+292>:	cmp    BYTE PTR [rcx+rax*1],0xc0
0x000055555555a588 <+296>:	jl     0x55555555ab21 <_ZN5rauth4main17h7d7aed61ae7734f4E+1729>
0x000055555555a58e <+302>:	mov    QWORD PTR [rsp+0x68],rax
0x000055555555a593 <+307>:	lea    rdi,[rsp+0xc8]
0x000055555555a59b <+315>:	lea    rsi,[rsp+0x58]
0x000055555555a5a0 <+320>:	call   QWORD PTR [rip+0x24563a]        # 0x55555579fbe0
0x000055555555a5a6 <+326>:	mov    rax,QWORD PTR [rsp+0xd8]
0x000055555555a5ae <+334>:	mov    QWORD PTR [rsp+0x80],rax
0x000055555555a5b6 <+342>:	movups xmm0,XMMWORD PTR [rsp+0xc8]
0x000055555555a5be <+350>:	movaps XMMWORD PTR [rsp+0x70],xmm0
0x000055555555a5c3 <+355>:	movaps xmm0,XMMWORD PTR [rip+0x336d6]        # 0x55555558dca0
0x000055555555a5ca <+362>:	movaps XMMWORD PTR [rsp+0x90],xmm0
0x000055555555a5d2 <+370>:	movdqa xmm0,XMMWORD PTR [rip+0x336d6]        # 0x55555558dcb0
0x000055555555a5da <+378>:	movdqa XMMWORD PTR [rsp+0xa0],xmm0
0x000055555555a5e3 <+387>:	movabs rax,0x3361303732633464
0x000055555555a5ed <+397>:	mov    QWORD PTR [rsp+0xc0],rax
0x000055555555a5f5 <+405>:	mov    edi,0x20
0x000055555555a5fa <+410>:	mov    esi,0x1
0x000055555555a5ff <+415>:	call   QWORD PTR [rip+0x2457a3]        # 0x55555579fda8
0x000055555555a605 <+421>:	test   rax,rax
0x000055555555a608 <+424>:	je     0x55555555aa82 <_ZN5rauth4main17h7d7aed61ae7734f4E+1570>
0x000055555555a60e <+430>:	mov    r15,rax
0x000055555555a611 <+433>:	movaps xmm0,XMMWORD PTR [rip+0x336a8]        # 0x55555558dcc0
0x000055555555a618 <+440>:	movups XMMWORD PTR [rax],xmm0
0x000055555555a61b <+443>:	movaps xmm0,XMMWORD PTR [rip+0x336ae]        # 0x55555558dcd0
0x000055555555a622 <+450>:	movups XMMWORD PTR [rax+0x10],xmm0
0x000055555555a626 <+454>:	mov    QWORD PTR [rsp+0x168],rax
0x000055555555a62e <+462>:	movdqa xmm0,XMMWORD PTR [rip+0x336aa]        # 0x55555558dce0
0x000055555555a636 <+470>:	movdqu XMMWORD PTR [rsp+0x170],xmm0
0x000055555555a63f <+479>:	mov    rdi,rsp
0x000055555555a642 <+482>:	lea    rsi,[rsp+0x90]
0x000055555555a64a <+490>:	lea    rdx,[rsp+0xc0]
0x000055555555a652 <+498>:	call   0x555555559900 <_ZN7salsa204core13Core$LT$R$GT$3new17h06163fbcdf79ba51E>
0x000055555555a657 <+503>:	movdqu xmm0,XMMWORD PTR [rsp]
0x000055555555a65c <+508>:	movdqu xmm1,XMMWORD PTR [rsp+0x10]
0x000055555555a662 <+514>:	movdqu xmm2,XMMWORD PTR [rsp+0x20]
0x000055555555a668 <+520>:	movups xmm3,XMMWORD PTR [rsp+0x30]
0x000055555555a66d <+525>:	movups XMMWORD PTR [rsp+0x100],xmm3
0x000055555555a675 <+533>:	movdqu XMMWORD PTR [rsp+0xf0],xmm2
0x000055555555a67e <+542>:	movdqu XMMWORD PTR [rsp+0xe0],xmm1
0x000055555555a687 <+551>:	movdqu XMMWORD PTR [rsp+0xd0],xmm0
0x000055555555a690 <+560>:	mov    QWORD PTR [rsp+0xc8],0x0
0x000055555555a69c <+572>:	pxor   xmm0,xmm0
0x000055555555a6a0 <+576>:	movdqu XMMWORD PTR [rsp+0x110],xmm0
0x000055555555a6a9 <+585>:	movdqu XMMWORD PTR [rsp+0x120],xmm0
0x000055555555a6b2 <+594>:	movdqu XMMWORD PTR [rsp+0x130],xmm0
0x000055555555a6bb <+603>:	movdqu XMMWORD PTR [rsp+0x140],xmm0
0x000055555555a6c4 <+612>:	mov    BYTE PTR [rsp+0x150],0x0
0x000055555555a6cc <+620>:	mov    r14,QWORD PTR [rsp+0x70]
0x000055555555a6d1 <+625>:	mov    r12,QWORD PTR [rsp+0x80]
0x000055555555a6d9 <+633>:	test   r12,r12
0x000055555555a6dc <+636>:	je     0x55555555a701 <_ZN5rauth4main17h7d7aed61ae7734f4E+673>
0x000055555555a6de <+638>:	mov    esi,0x1
0x000055555555a6e3 <+643>:	mov    rdi,r12
0x000055555555a6e6 <+646>:	call   QWORD PTR [rip+0x2456bc]        # 0x55555579fda8
0x000055555555a6ec <+652>:	test   rax,rax
0x000055555555a6ef <+655>:	jne    0x55555555a706 <_ZN5rauth4main17h7d7aed61ae7734f4E+678>
0x000055555555a6f1 <+657>:	mov    esi,0x1
0x000055555555a6f6 <+662>:	mov    rdi,r12
0x000055555555a6f9 <+665>:	call   QWORD PTR [rip+0x2457d1]        # 0x55555579fed0
0x000055555555a6ff <+671>:	ud2    
0x000055555555a701 <+673>:	mov    eax,0x1
0x000055555555a706 <+678>:	mov    QWORD PTR [rsp+0x40],rax
0x000055555555a70b <+683>:	mov    QWORD PTR [rsp+0x48],r12
0x000055555555a710 <+688>:	mov    QWORD PTR [rsp+0x50],0x0
0x000055555555a719 <+697>:	lea    rdi,[rsp+0x40]
0x000055555555a71e <+702>:	xor    esi,esi
0x000055555555a720 <+704>:	mov    rdx,r12
0x000055555555a723 <+707>:	call   0x555555559620 <_ZN5alloc7raw_vec19RawVec$LT$T$C$A$GT$7reserve17h37e7c2e36f33cad8E>
0x000055555555a728 <+712>:	mov    rbx,QWORD PTR [rsp+0x50]
0x000055555555a72d <+717>:	mov    rdi,QWORD PTR [rsp+0x40]
0x000055555555a732 <+722>:	add    rdi,rbx
0x000055555555a735 <+725>:	mov    rsi,r14
0x000055555555a738 <+728>:	mov    rdx,r12
0x000055555555a73b <+731>:	call   QWORD PTR [rip+0x245867]        # 0x55555579ffa8
0x000055555555a741 <+737>:	add    rbx,r12
0x000055555555a744 <+740>:	mov    QWORD PTR [rsp+0x50],rbx
0x000055555555a749 <+745>:	mov    rsi,QWORD PTR [rsp+0x40]
0x000055555555a74e <+750>:	lea    rdi,[rsp+0xc8]
0x000055555555a756 <+758>:	mov    rdx,rbx
0x000055555555a759 <+761>:	call   0x555555559d10 <_ZN79_$LT$salsa20..salsa..Salsa$LT$R$GT$$u20$as$u20$cipher..stream..StreamCipher$GT$19try_apply_keystream17hdbdc0561b68e3b6aE>
0x000055555555a75e <+766>:	test   al,al
0x000055555555a760 <+768>:	jne    0x55555555aa89 <_ZN5rauth4main17h7d7aed61ae7734f4E+1577>
0x000055555555a766 <+774>:	mov    r12,QWORD PTR [rsp+0x40]
0x000055555555a76b <+779>:	mov    rbx,QWORD PTR [rsp+0x50]
0x000055555555a770 <+784>:	test   rbx,rbx
0x000055555555a773 <+787>:	je     0x55555555a798 <_ZN5rauth4main17h7d7aed61ae7734f4E+824>
0x000055555555a775 <+789>:	mov    esi,0x1
0x000055555555a77a <+794>:	mov    rdi,rbx
0x000055555555a77d <+797>:	call   QWORD PTR [rip+0x245625]        # 0x55555579fda8
0x000055555555a783 <+803>:	test   rax,rax
0x000055555555a786 <+806>:	jne    0x55555555a79d <_ZN5rauth4main17h7d7aed61ae7734f4E+829>
0x000055555555a788 <+808>:	mov    esi,0x1
0x000055555555a78d <+813>:	mov    rdi,rbx
0x000055555555a790 <+816>:	call   QWORD PTR [rip+0x24573a]        # 0x55555579fed0
0x000055555555a796 <+822>:	ud2    
0x000055555555a798 <+824>:	mov    eax,0x1
0x000055555555a79d <+829>:	mov    QWORD PTR [rsp],rax
0x000055555555a7a1 <+833>:	mov    QWORD PTR [rsp+0x8],rbx
0x000055555555a7a6 <+838>:	mov    QWORD PTR [rsp+0x10],0x0
0x000055555555a7af <+847>:	mov    rdi,rsp
0x000055555555a7b2 <+850>:	xor    esi,esi
0x000055555555a7b4 <+852>:	mov    rdx,rbx
0x000055555555a7b7 <+855>:	call   0x555555559620 <_ZN5alloc7raw_vec19RawVec$LT$T$C$A$GT$7reserve17h37e7c2e36f33cad8E>
0x000055555555a7bc <+860>:	mov    rbp,QWORD PTR [rsp+0x10]
0x000055555555a7c1 <+865>:	mov    rdi,QWORD PTR [rsp]
0x000055555555a7c5 <+869>:	add    rdi,rbp
0x000055555555a7c8 <+872>:	mov    rsi,r12
0x000055555555a7cb <+875>:	mov    rdx,rbx
0x000055555555a7ce <+878>:	call   QWORD PTR [rip+0x2457d4]        # 0x55555579ffa8
0x000055555555a7d4 <+884>:	add    rbp,rbx
0x000055555555a7d7 <+887>:	mov    QWORD PTR [rsp+0x10],rbp
0x000055555555a7dc <+892>:	mov    rdi,QWORD PTR [rsp]
0x000055555555a7e0 <+896>:	cmp    rbp,0x20
0x000055555555a7e4 <+900>:	jne    0x55555555a827 <_ZN5rauth4main17h7d7aed61ae7734f4E+967>
0x000055555555a7e6 <+902>:	cmp    rdi,r15
0x000055555555a7e9 <+905>:	je     0x55555555aa37 <_ZN5rauth4main17h7d7aed61ae7734f4E+1495>
0x000055555555a7ef <+911>:	movdqu xmm0,XMMWORD PTR [r15]
0x000055555555a7f4 <+916>:	movdqu xmm1,XMMWORD PTR [r15+0x10]
0x000055555555a7fa <+922>:	movdqu xmm2,XMMWORD PTR [rdi]
0x000055555555a7fe <+926>:	pcmpeqb xmm2,xmm0
0x000055555555a802 <+930>:	movdqu xmm0,XMMWORD PTR [rdi+0x10]
0x000055555555a807 <+935>:	pcmpeqb xmm0,xmm1
0x000055555555a80b <+939>:	pand   xmm0,xmm2
0x000055555555a80f <+943>:	pmovmskb eax,xmm0
0x000055555555a813 <+947>:	cmp    eax,0xffff
0x000055555555a818 <+952>:	sete   bl
0x000055555555a81b <+955>:	mov    rsi,QWORD PTR [rsp+0x8]
0x000055555555a820 <+960>:	test   rsi,rsi
0x000055555555a823 <+963>:	jne    0x55555555a833 <_ZN5rauth4main17h7d7aed61ae7734f4E+979>
0x000055555555a825 <+965>:	jmp    0x55555555a83e <_ZN5rauth4main17h7d7aed61ae7734f4E+990>
0x000055555555a827 <+967>:	xor    ebx,ebx
0x000055555555a829 <+969>:	mov    rsi,QWORD PTR [rsp+0x8]
0x000055555555a82e <+974>:	test   rsi,rsi
0x000055555555a831 <+977>:	je     0x55555555a83e <_ZN5rauth4main17h7d7aed61ae7734f4E+990>
0x000055555555a833 <+979>:	mov    edx,0x1
0x000055555555a838 <+984>:	call   QWORD PTR [rip+0x24538a]        # 0x55555579fbc8
0x000055555555a83e <+990>:	test   bl,bl
0x000055555555a840 <+992>:	je     0x55555555a992 <_ZN5rauth4main17h7d7aed61ae7734f4E+1330>
0x000055555555a846 <+998>:	lea    rax,[rip+0x242933]        # 0x55555579d180
0x000055555555a84d <+1005>:	mov    QWORD PTR [rsp],rax
0x000055555555a851 <+1009>:	mov    QWORD PTR [rsp+0x8],0x1
0x000055555555a85a <+1018>:	mov    QWORD PTR [rsp+0x10],0x0
0x000055555555a863 <+1027>:	mov    QWORD PTR [rsp+0x20],r13
0x000055555555a868 <+1032>:	mov    QWORD PTR [rsp+0x28],0x0
0x000055555555a871 <+1041>:	mov    rdi,rsp
0x000055555555a874 <+1044>:	call   QWORD PTR [rip+0x245766]        # 0x55555579ffe0
0x000055555555a87a <+1050>:	mov    QWORD PTR [rsp+0xc8],0x0
0x000055555555a886 <+1062>:	mov    BYTE PTR [rsp+0x150],0x0
0x000055555555a88e <+1070>:	mov    edi,0x18
0x000055555555a893 <+1075>:	mov    esi,0x1
0x000055555555a898 <+1080>:	call   QWORD PTR [rip+0x24550a]        # 0x55555579fda8
0x000055555555a89e <+1086>:	test   rax,rax
0x000055555555a8a1 <+1089>:	je     0x55555555aab1 <_ZN5rauth4main17h7d7aed61ae7734f4E+1617>
0x000055555555a8a7 <+1095>:	mov    rbx,rax
0x000055555555a8aa <+1098>:	movaps xmm0,XMMWORD PTR [rip+0x3343f]        # 0x55555558dcf0
0x000055555555a8b1 <+1105>:	movups XMMWORD PTR [rax],xmm0
0x000055555555a8b4 <+1108>:	movabs rax,0x61e281c563371937
0x000055555555a8be <+1118>:	mov    QWORD PTR [rbx+0x10],rax
0x000055555555a8c2 <+1122>:	mov    QWORD PTR [rsp+0x180],rbx
0x000055555555a8ca <+1130>:	movdqa xmm0,XMMWORD PTR [rip+0x3342e]        # 0x55555558dd00
0x000055555555a8d2 <+1138>:	movdqu XMMWORD PTR [rsp+0x188],xmm0
0x000055555555a8db <+1147>:	lea    rdi,[rsp+0xc8]
0x000055555555a8e3 <+1155>:	mov    edx,0x18
0x000055555555a8e8 <+1160>:	mov    rsi,rbx
0x000055555555a8eb <+1163>:	call   0x555555559d10 <_ZN79_$LT$salsa20..salsa..Salsa$LT$R$GT$$u20$as$u20$cipher..stream..StreamCipher$GT$19try_apply_keystream17hdbdc0561b68e3b6aE>
0x000055555555a8f0 <+1168>:	test   al,al
0x000055555555a8f2 <+1170>:	jne    0x55555555aac3 <_ZN5rauth4main17h7d7aed61ae7734f4E+1635>
0x000055555555a8f8 <+1176>:	mov    rdi,rsp
0x000055555555a8fb <+1179>:	mov    edx,0x18
0x000055555555a900 <+1184>:	mov    rsi,rbx
0x000055555555a903 <+1187>:	call   QWORD PTR [rip+0x245337]        # 0x55555579fc40
0x000055555555a909 <+1193>:	cmp    DWORD PTR [rsp],0x1
0x000055555555a90d <+1197>:	je     0x55555555aae8 <_ZN5rauth4main17h7d7aed61ae7734f4E+1672>
0x000055555555a913 <+1203>:	movdqu xmm0,XMMWORD PTR [rsp+0x8]
0x000055555555a919 <+1209>:	movdqa XMMWORD PTR [rsp+0xb0],xmm0
0x000055555555a922 <+1218>:	lea    rax,[rsp+0xb0]
0x000055555555a92a <+1226>:	mov    QWORD PTR [rsp+0x158],rax
0x000055555555a932 <+1234>:	lea    rax,[rip+0xfffffffffffff377]        # 0x555555559cb0 <_ZN42_$LT$$RF$T$u20$as$u20$core..fmt..Debug$GT$3fmt17hf726897ee99deccaE>
0x000055555555a939 <+1241>:	mov    QWORD PTR [rsp+0x160],rax
0x000055555555a941 <+1249>:	lea    rax,[rip+0x242848]        # 0x55555579d190
0x000055555555a948 <+1256>:	mov    QWORD PTR [rsp],rax
0x000055555555a94c <+1260>:	mov    QWORD PTR [rsp+0x8],0x2
0x000055555555a955 <+1269>:	mov    QWORD PTR [rsp+0x10],0x0
0x000055555555a95e <+1278>:	lea    rax,[rsp+0x158]
0x000055555555a966 <+1286>:	mov    QWORD PTR [rsp+0x20],rax
0x000055555555a96b <+1291>:	mov    QWORD PTR [rsp+0x28],0x1
0x000055555555a974 <+1300>:	mov    rdi,rsp
0x000055555555a977 <+1303>:	call   QWORD PTR [rip+0x245663]        # 0x55555579ffe0
0x000055555555a97d <+1309>:	mov    esi,0x18
0x000055555555a982 <+1314>:	mov    edx,0x1
0x000055555555a987 <+1319>:	mov    rdi,rbx
0x000055555555a98a <+1322>:	call   QWORD PTR [rip+0x245238]        # 0x55555579fbc8
0x000055555555a990 <+1328>:	jmp    0x55555555a9c6 <_ZN5rauth4main17h7d7aed61ae7734f4E+1382>
0x000055555555a992 <+1330>:	lea    rax,[rip+0x24282f]        # 0x55555579d1c8
0x000055555555a999 <+1337>:	mov    QWORD PTR [rsp],rax
0x000055555555a99d <+1341>:	mov    QWORD PTR [rsp+0x8],0x1
0x000055555555a9a6 <+1350>:	mov    QWORD PTR [rsp+0x10],0x0
0x000055555555a9af <+1359>:	mov    QWORD PTR [rsp+0x20],r13
0x000055555555a9b4 <+1364>:	mov    QWORD PTR [rsp+0x28],0x0
0x000055555555a9bd <+1373>:	mov    rdi,rsp
0x000055555555a9c0 <+1376>:	call   QWORD PTR [rip+0x24561a]        # 0x55555579ffe0
0x000055555555a9c6 <+1382>:	mov    rsi,QWORD PTR [rsp+0x48]
0x000055555555a9cb <+1387>:	test   rsi,rsi
0x000055555555a9ce <+1390>:	je     0x55555555a9e0 <_ZN5rauth4main17h7d7aed61ae7734f4E+1408>
0x000055555555a9d0 <+1392>:	mov    rdi,QWORD PTR [rsp+0x40]
0x000055555555a9d5 <+1397>:	mov    edx,0x1
0x000055555555a9da <+1402>:	call   QWORD PTR [rip+0x2451e8]        # 0x55555579fbc8
0x000055555555a9e0 <+1408>:	mov    esi,0x20
0x000055555555a9e5 <+1413>:	mov    edx,0x1
0x000055555555a9ea <+1418>:	mov    rdi,r15
0x000055555555a9ed <+1421>:	call   QWORD PTR [rip+0x2451d5]        # 0x55555579fbc8
0x000055555555a9f3 <+1427>:	mov    rsi,QWORD PTR [rsp+0x78]
0x000055555555a9f8 <+1432>:	test   rsi,rsi
0x000055555555a9fb <+1435>:	je     0x55555555aa0b <_ZN5rauth4main17h7d7aed61ae7734f4E+1451>
0x000055555555a9fd <+1437>:	mov    edx,0x1
0x000055555555aa02 <+1442>:	mov    rdi,r14
0x000055555555aa05 <+1445>:	call   QWORD PTR [rip+0x2451bd]        # 0x55555579fbc8
0x000055555555aa0b <+1451>:	mov    rsi,QWORD PTR [rsp+0x60]
0x000055555555aa10 <+1456>:	test   rsi,rsi
0x000055555555aa13 <+1459>:	je     0x55555555aa25 <_ZN5rauth4main17h7d7aed61ae7734f4E+1477>
0x000055555555aa15 <+1461>:	mov    rdi,QWORD PTR [rsp+0x58]
0x000055555555aa1a <+1466>:	mov    edx,0x1
0x000055555555aa1f <+1471>:	call   QWORD PTR [rip+0x2451a3]        # 0x55555579fbc8
0x000055555555aa25 <+1477>:	add    rsp,0x198
0x000055555555aa2c <+1484>:	pop    rbx
0x000055555555aa2d <+1485>:	pop    r12
0x000055555555aa2f <+1487>:	pop    r13
0x000055555555aa31 <+1489>:	pop    r14
0x000055555555aa33 <+1491>:	pop    r15
0x000055555555aa35 <+1493>:	pop    rbp
0x000055555555aa36 <+1494>:	ret    
0x000055555555aa37 <+1495>:	mov    bl,0x1
0x000055555555aa39 <+1497>:	mov    rsi,QWORD PTR [rsp+0x8]
0x000055555555aa3e <+1502>:	test   rsi,rsi
0x000055555555aa41 <+1505>:	jne    0x55555555a833 <_ZN5rauth4main17h7d7aed61ae7734f4E+979>
0x000055555555aa47 <+1511>:	jmp    0x55555555a83e <_ZN5rauth4main17h7d7aed61ae7734f4E+990>
0x000055555555aa4c <+1516>:	movdqu xmm0,XMMWORD PTR [rsp+0xd0]
0x000055555555aa55 <+1525>:	movdqa XMMWORD PTR [rsp],xmm0
0x000055555555aa5a <+1530>:	lea    rdi,[rip+0x33441]        # 0x55555558dea2
0x000055555555aa61 <+1537>:	lea    rcx,[rip+0x242688]        # 0x55555579d0f0
0x000055555555aa68 <+1544>:	lea    r8,[rip+0x242789]        # 0x55555579d1f8
0x000055555555aa6f <+1551>:	mov    rdx,rsp
0x000055555555aa72 <+1554>:	mov    esi,0x15
0x000055555555aa77 <+1559>:	call   QWORD PTR [rip+0x24538b]        # 0x55555579fe08
0x000055555555aa7d <+1565>:	jmp    0x55555555ab3a <_ZN5rauth4main17h7d7aed61ae7734f4E+1754>
0x000055555555aa82 <+1570>:	mov    edi,0x20
0x000055555555aa87 <+1575>:	jmp    0x55555555aab6 <_ZN5rauth4main17h7d7aed61ae7734f4E+1622>
0x000055555555aa89 <+1577>:	lea    rdi,[rip+0x33280]        # 0x55555558dd10
0x000055555555aa90 <+1584>:	lea    rcx,[rip+0x242679]        # 0x55555579d110
0x000055555555aa97 <+1591>:	lea    r8,[rip+0x2426ca]        # 0x55555579d168
0x000055555555aa9e <+1598>:	mov    rdx,rsp
0x000055555555aaa1 <+1601>:	mov    esi,0x2b
0x000055555555aaa6 <+1606>:	call   QWORD PTR [rip+0x24535c]        # 0x55555579fe08
0x000055555555aaac <+1612>:	jmp    0x55555555ab3a <_ZN5rauth4main17h7d7aed61ae7734f4E+1754>
0x000055555555aab1 <+1617>:	mov    edi,0x18
0x000055555555aab6 <+1622>:	mov    esi,0x1
0x000055555555aabb <+1627>:	call   QWORD PTR [rip+0x24540f]        # 0x55555579fed0
0x000055555555aac1 <+1633>:	ud2    
0x000055555555aac3 <+1635>:	lea    rdi,[rip+0x33246]        # 0x55555558dd10
0x000055555555aaca <+1642>:	lea    rcx,[rip+0x24263f]        # 0x55555579d110
0x000055555555aad1 <+1649>:	lea    r8,[rip+0x242690]        # 0x55555579d168
0x000055555555aad8 <+1656>:	mov    rdx,rsp
0x000055555555aadb <+1659>:	mov    esi,0x2b
0x000055555555aae0 <+1664>:	call   QWORD PTR [rip+0x245322]        # 0x55555579fe08
0x000055555555aae6 <+1670>:	jmp    0x55555555ab3a <_ZN5rauth4main17h7d7aed61ae7734f4E+1754>
0x000055555555aae8 <+1672>:	movdqu xmm0,XMMWORD PTR [rsp+0x8]
0x000055555555aaee <+1678>:	movdqa XMMWORD PTR [rsp+0xb0],xmm0
0x000055555555aaf7 <+1687>:	lea    rdi,[rip+0x33212]        # 0x55555558dd10
0x000055555555aafe <+1694>:	lea    rcx,[rip+0x24262b]        # 0x55555579d130
0x000055555555ab05 <+1701>:	lea    r8,[rip+0x2426a4]        # 0x55555579d1b0
0x000055555555ab0c <+1708>:	lea    rdx,[rsp+0xb0]
0x000055555555ab14 <+1716>:	mov    esi,0x2b
0x000055555555ab19 <+1721>:	call   QWORD PTR [rip+0x2452e9]        # 0x55555579fe08
0x000055555555ab1f <+1727>:	jmp    0x55555555ab3a <_ZN5rauth4main17h7d7aed61ae7734f4E+1754>
0x000055555555ab21 <+1729>:	lea    rdi,[rip+0x33213]        # 0x55555558dd3b
0x000055555555ab28 <+1736>:	lea    rdx,[rip+0x242621]        # 0x55555579d150
0x000055555555ab2f <+1743>:	mov    esi,0x30
0x000055555555ab34 <+1748>:	call   QWORD PTR [rip+0x24502e]        # 0x55555579fb68
0x000055555555ab3a <+1754>:	ud2    
0x000055555555ab3c <+1756>:	mov    rbx,rax
0x000055555555ab3f <+1759>:	mov    rdi,rsp
0x000055555555ab42 <+1762>:	call   0x55555555a370 <_ZN4core3ptr13drop_in_place17hb9be5e79ad71d74aE>
0x000055555555ab47 <+1767>:	jmp    0x55555555ab6d <_ZN5rauth4main17h7d7aed61ae7734f4E+1805>
0x000055555555ab49 <+1769>:	mov    rbx,rax
0x000055555555ab4c <+1772>:	mov    rdi,rsp
0x000055555555ab4f <+1775>:	call   0x55555555a3f0 <_ZN4core3ptr13drop_in_place17he17cde9f03ccb532E>
0x000055555555ab54 <+1780>:	jmp    0x55555555ab91 <_ZN5rauth4main17h7d7aed61ae7734f4E+1841>
0x000055555555ab56 <+1782>:	mov    rbx,rax
0x000055555555ab59 <+1785>:	lea    rdi,[rsp+0x40]
0x000055555555ab5e <+1790>:	call   0x55555555ac00 <_ZN4core3ptr13drop_in_place17he17cde9f03ccb532E.llvm.10920103316688273462>
0x000055555555ab63 <+1795>:	jmp    0x55555555ab9b <_ZN5rauth4main17h7d7aed61ae7734f4E+1851>
0x000055555555ab65 <+1797>:	mov    rbx,rax
0x000055555555ab68 <+1800>:	jmp    0x55555555ab9b <_ZN5rauth4main17h7d7aed61ae7734f4E+1851>
0x000055555555ab6a <+1802>:	mov    rbx,rax
0x000055555555ab6d <+1805>:	lea    rdi,[rsp+0x90]
0x000055555555ab75 <+1813>:	call   0x55555555a350 <_ZN4core3ptr13drop_in_place17h08d2eaa22c38a960E>
0x000055555555ab7a <+1818>:	jmp    0x55555555abbc <_ZN5rauth4main17h7d7aed61ae7734f4E+1884>
0x000055555555ab7c <+1820>:	mov    rbx,rax
0x000055555555ab7f <+1823>:	lea    rdi,[rsp+0x180]
0x000055555555ab87 <+1831>:	call   0x55555555a3f0 <_ZN4core3ptr13drop_in_place17he17cde9f03ccb532E>
0x000055555555ab8c <+1836>:	jmp    0x55555555ab91 <_ZN5rauth4main17h7d7aed61ae7734f4E+1841>
0x000055555555ab8e <+1838>:	mov    rbx,rax
0x000055555555ab91 <+1841>:	lea    rdi,[rsp+0x40]
0x000055555555ab96 <+1846>:	call   0x55555555a3f0 <_ZN4core3ptr13drop_in_place17he17cde9f03ccb532E>
0x000055555555ab9b <+1851>:	lea    rdi,[rsp+0x168]
0x000055555555aba3 <+1859>:	call   0x55555555a3f0 <_ZN4core3ptr13drop_in_place17he17cde9f03ccb532E>
0x000055555555aba8 <+1864>:	lea    rdi,[rsp+0x70]
0x000055555555abad <+1869>:	call   0x55555555a3f0 <_ZN4core3ptr13drop_in_place17he17cde9f03ccb532E>
0x000055555555abb2 <+1874>:	jmp    0x55555555abbc <_ZN5rauth4main17h7d7aed61ae7734f4E+1884>
0x000055555555abb4 <+1876>:	mov    rbx,rax
0x000055555555abb7 <+1879>:	jmp    0x55555555aba8 <_ZN5rauth4main17h7d7aed61ae7734f4E+1864>
0x000055555555abb9 <+1881>:	mov    rbx,rax
0x000055555555abbc <+1884>:	lea    rdi,[rsp+0x58]
0x000055555555abc1 <+1889>:	call   0x55555555a410 <_ZN4core3ptr13drop_in_place17heafee118800ce503E>
0x000055555555abc6 <+1894>:	mov    rdi,rbx
0x000055555555abc9 <+1897>:	call   0x5555555594f0 <_Unwind_Resume@plt>
0x000055555555abce <+1902>:	ud2