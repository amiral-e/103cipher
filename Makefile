##
## EPITECH PROJECT, 2020
## 102architect
## File description:
## Makefile
##

### SOURCES ###
#----c_sources----#
SRC			:= 103cipher.py
### SOURCES ###


### COMPILE_USEFULL ###
#----project_usefull----#
NAME		=	103cipher
MAKEFLAGS 	+=	--no-print-directory
### COMPILE_USEFULL ###


### COLORS ###
ccred		= /bin/echo -e "\x1b[1m\x1b[33m\#\#\x1b[31m $1\033[0m"
ccyellow	= /bin/echo -e "\x1b[1m\x1b[33m\#\#\x1b[33m $1\033[0m"
ccend		= /bin/echo -e "\x1b[1m\x1b[33m\#\#\x1b[32m $1\033[0m"
### COLORS ###


#------------------------------------------------------------#
.PHONY:		all
all:		$(NAME)
$(NAME):
			cp $(SRC) $(NAME)
			chmod +x $(NAME)
			@$(call ccend, "Lib successfully compiled.")

#------------------------------------------------------------#
.PHONY:		tests_run
tests_run:	fclean
			coverage run -m unittest discover test/ -v -b
			coverage report -m 
			@$(call ccend, "Unit tests successfully compiled.")

#------------------------------------------------------------#
.PHONY:		clean
clean:
			$(RM) -rf src/__pycache__ test/__pycache__ .coverage
			@$(call ccyellow, "Lib cleaned.")

#------------------------------------------------------------#
.PHONY:		fclean
fclean:		clean
			$(RM) $(NAME)
			@$(call ccred, "Lib fully cleaned.")

#------------------------------------------------------------#
.PHONY:		re
re:			fclean all