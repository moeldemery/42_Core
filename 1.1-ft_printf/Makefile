CC = cc
CFLAGS = -Wall -Wextra -Werror

# Define the archiver and flags for creating/updating the archive
AR = ar
ARFLAGS = rcs

SRCS = \
	ft_printf.c \
	ft_putnbr_base.c

BONUS = \
	ft_printf_bonus.c \
	ft_putnbr_base_bonus.c \
	ft_printf_util_bonus.c \
	ft_printf_util_b_bonus.c 

NAME = libftprintf.a
OBJS = $(SRCS:.c=.o)
OBJS_BONUS = $(BONUS:.c=.o)
LIBFT_LIB = libft/libft.a

all: $(NAME)

$(NAME): $(OBJS) libft
	cp $(LIBFT_LIB) $(NAME)
	$(AR) $(ARFLAGS) $(NAME) $(OBJS)

%.o: %.c 
	$(CC) -c $(CFLAGS)  $< -o $@
	
libft:
	make -C libft

bonus: $(OBJS_BONUS) libft
	cp $(LIBFT_LIB) $(NAME)
	$(AR) $(ARFLAGS) $(NAME) $(OBJS_BONUS)

clean:
	rm -f $(OBJS)
	rm -f $(OBJS_BONUS)
	make -C libft clean
	
fclean: clean
	rm -f $(NAME) libft/libft.a

re: fclean all

.PHONY: all libft clean fclean re BONUS
