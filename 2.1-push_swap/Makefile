CC = cc
CFLAGS = -Wall -Wextra -Werror

SRCS = \



NAME = push_swap
OBJS = $(SRCS:.c=.o)
LIBFT_LIB = libft/libft.a

all: $(NAME)

$(NAME): $(OBJS) libft
	$(CC) $(CFLAGS)  $@.c $(LIBFT_LIB) -o $@.o


%.o: %.c 
	$(CC) -c $(CFLAGS)  $< -o $@
	
libft:
	make -C libft


clean:
	rm -f $(OBJS)
	rm -f $(OBJS_BONUS)
	make -C libft clean
	
fclean: clean
	rm -f $(NAME) libft/libft.a

re: fclean all

.PHONY: all libft clean fclean re 
