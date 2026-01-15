CC = cc
CFLAGS = #-Wall -Wextra -Werror

SRCS = 	stack_sort_algo.c stack_sort_algo_n.c\
		stack_cmd_a.c  stack_cmd_b.c  stack_cmd_c.c \
		stack_operations.c  \
	   	stack_util_a.c  stack_util_b.c \
		debug_util.c \
		lis_calc.c lis_set_mask.c \
		stack_calc_cost.c stack_execute_cost.c \




NAME = push_swap
OBJS = $(SRCS:.c=.o)
LIBFT_LIB = libft/libft.a

all: $(NAME)

$(NAME): $(OBJS) $(libft)
	make -C libft
	$(CC) $(CFLAGS)  $@.c $^ $(LIBFT_LIB) -o $@


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
