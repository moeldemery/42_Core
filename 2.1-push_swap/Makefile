CC = cc
CFLAGS = -Wall -Wextra -Werror

SRCS = 	stack_sort_algo.c stack_sort_algo_n.c\
		stack_cmd_a.c  stack_cmd_b.c  stack_cmd_c.c \
		stack_operations.c  \
	   	stack_util_a.c  stack_util_b.c \
		debug_util.c arg_support.c\
		lis_calc.c lis_set_mask.c \
		stack_calc_cost.c stack_execute_cost.c

BONUS_SRCS = debug_util.c arg_support.c\
		stack_cmd_a.c  stack_cmd_b.c  stack_cmd_c.c \
		stack_operations.c  \
		stack_util_a.c  stack_util_b.c


NAME = push_swap
OBJS = $(SRCS:.c=.o)
LIBFT_LIB = libft/libft.a
OBJS_BONUS = $(BONUS_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS) $(libft)
	make -C libft
	$(CC) $(CFLAGS)  $@.c $^ $(LIBFT_LIB) -o $@


%.o: %.c 
	$(CC) -c $(CFLAGS)  $< -o $@
	
libft:
	make -C libft

bonus:$(OBJS_BONUS) $(libft)
	make -C libft
	$(CC) $(CFLAGS)  checker_bonus.c $^ $(LIBFT_LIB) -o checker

clean:
	rm -f $(OBJS)
	rm -f $(OBJS_BONUS)
	make -C libft clean
	
fclean: clean
	rm -f $(NAME) libft/libft.a checker

re: fclean all

.PHONY: all libft clean fclean re 
