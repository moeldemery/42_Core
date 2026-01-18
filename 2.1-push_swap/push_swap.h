/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 15:28:17 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 15:28:19 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "arg_support.h"
# include "libft/ft_printf.h"
# include "libft/libft.h"
# include <stdlib.h>
# include <unistd.h>

# define DEBUG 0
# define MAX_INT 2147483647

typedef struct s_element
{
	int		value;
	int		lis_cost;
	int		lis_mask;
	int		cost;
	int		cost_a;
	int		cost_b;
}			t_element;

/* Debugging functions *********************************************/
int			ft_list_print(t_d_list *lst, int is_enabled, char *msg);
int			ft_list_print_liscost(t_d_list *lst, int is_enabled, char *msg);
int			ft_list_print_lismask(t_d_list *lst, int is_enabled, char *msg);
int			ft_list_print_costs(t_d_list *lst, int is_enabled, char *msg);
int			ft_print_index_costs(t_d_list *lst, int index, int is_enabled,
				char *msg);
/*stack_operations****************************************************/
void		ft_stack_swap(t_d_list **stack);
void		ft_stack_push(t_d_list **src, t_d_list **dest);
void		ft_stack_rotate(t_d_list **stack);
void		ft_stack_reverse_rotate(t_d_list **stack);
/*stack_cmd_a****************************************************/
void		ft_sa(t_d_list **stack_a);
void		ft_pa(t_d_list **stack_a, t_d_list **stack_b);
void		ft_ra(t_d_list **stack_a);
void		ft_rra(t_d_list **stack_a);
/*stack_cmd_b****************************************************/
void		ft_sb(t_d_list **stack_b);
void		ft_pb(t_d_list **stack_a, t_d_list **stack_b);
void		ft_rb(t_d_list **stack_b);
void		ft_rrb(t_d_list **stack_b);
/*stack_cmd_c***************************************************/
void		ft_ss(t_d_list **stack_a, t_d_list **stack_b);
void		ft_rr(t_d_list **stack_a, t_d_list **stack_b);
void		ft_rrr(t_d_list **stack_a, t_d_list **stack_b);
/*stack_sort_algo****************************************************/
int			ft_sort_stack(t_d_list **stack_a, t_d_list **stack_b);
void		ft_sort_three(t_d_list **stack);
void		ft_sort_four(t_d_list **stack_a, t_d_list **stack_b);
void		ft_sort_five(t_d_list **stack_a, t_d_list **stack_b);
void		ft_sort_n(t_d_list **stack_a, t_d_list **stack_b, int size);
/*stack_util_a***************************************************/
int			ft_is_sorted(t_d_list *stack);
int			ft_is_str_digit(char *str);
t_element	*ft_init_element(int value);
int			ft_find_min(t_d_list *stack, int is_debug);
int			ft_find_max(t_d_list *stack, int is_debug);
/*stack_sort_algo_n***************************************************/
int			ft_find_lis(t_d_list **stack_a, int size);
void		ft_push_non_lis(t_d_list **stack_a, t_d_list **stack_b, int size,
				int lis_len);
void		ft_sort_remaining(t_d_list **stack_a, t_d_list **stack_b);
void		ft_final_rotate(t_d_list **stack_a);
/*lis_calc***************************************************/
int			ft_calculate_lis(t_d_list **stack_a, int size);
/*lis_set_mask***************************************************/
void		ft_set_max_lis_mask(t_d_list *stack_a, int max_len);
/*stack_sort_cost**********************************************/
void		ft_reset_costs(t_d_list *stack_b);
int			ft_get_combined_cost(int a, int b);
void		ft_calculate_costs(t_d_list **stack_a, t_d_list **stack_b,
				int size_a, int size_b);
/*stack_execute_cost*******************************************/
t_d_list	*ft_get_element_at_index(t_d_list *stack, int index);
void		ft_execute_cheapest_move(t_d_list **stack_a, t_d_list **stack_b);

/*stack_util_b***************************************************/
int			ft_find_min_index(t_d_list *stack);
int			ft_find_insert_position(t_d_list *stack_a, int value);
int			ft_find_cheapest_index(t_d_list *stack_b);
void		free_stack(t_d_list **stack);

#endif