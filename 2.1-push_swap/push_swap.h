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
int			ft_list_print(td_list *lst, int is_enabled, char *msg);
int			ft_list_print_liscost(td_list *lst, int is_enabled, char *msg);
int			ft_list_print_lismask(td_list *lst, int is_enabled, char *msg);
int			ft_list_print_costs(td_list *lst, int is_enabled, char *msg);
int			ft_print_index_costs(td_list *lst, int index, int is_enabled,
				char *msg);
/*stack_operations****************************************************/
void		ft_stack_swap(td_list **stack);
void		ft_stack_push(td_list **src, td_list **dest);
void		ft_stack_rotate(td_list **stack);
void		ft_stack_reverse_rotate(td_list **stack);
/*stack_cmd_a****************************************************/
void		ft_sa(td_list **stack_a);
void		ft_pa(td_list **stack_a, td_list **stack_b);
void		ft_ra(td_list **stack_a);
void		ft_rra(td_list **stack_a);
/*stack_cmd_b****************************************************/
void		ft_sb(td_list **stack_b);
void		ft_pb(td_list **stack_a, td_list **stack_b);
void		ft_rb(td_list **stack_b);
void		ft_rrb(td_list **stack_b);
/*stack_cmd_c***************************************************/
void		ft_ss(td_list **stack_a, td_list **stack_b);
void		ft_rr(td_list **stack_a, td_list **stack_b);
void		ft_rrr(td_list **stack_a, td_list **stack_b);
/*stack_sort_algo****************************************************/
int			ft_sort_stack(td_list **stack_a, td_list **stack_b);
void		ft_sort_three(td_list **stack);
void		ft_sort_four(td_list **stack_a, td_list **stack_b);
void		ft_sort_five(td_list **stack_a, td_list **stack_b);
void		ft_sort_n(td_list **stack_a, td_list **stack_b, int size);
/*stack_util_a***************************************************/
int			ft_is_sorted(td_list *stack);
int			ft_is_str_digit(char *str);
t_element	*ft_init_element(int value);
int			ft_find_min(td_list *stack, int is_debug);
int			ft_find_max(td_list *stack, int is_debug);
/*stack_sort_algo_n***************************************************/
int			ft_find_lis(td_list **stack_a, int size);
void		ft_push_non_lis(td_list **stack_a, td_list **stack_b, int size,
				int lis_len);
void		ft_sort_remaining(td_list **stack_a, td_list **stack_b);
void		ft_final_rotate(td_list **stack_a);
/*lis_calc***************************************************/
int			ft_calculate_lis(td_list **stack_a, int size);
/*lis_set_mask***************************************************/
void		ft_set_max_lis_mask(td_list *stack_a, int max_len);
/*stack_sort_cost**********************************************/
void		ft_reset_costs(td_list *stack_b);
int			ft_get_combined_cost(int a, int b);
void		ft_calculate_costs(td_list **stack_a, td_list **stack_b, int size_a,
				int size_b);
/*stack_execute_cost*******************************************/
td_list		*ft_get_element_at_index(td_list *stack, int index);
void		ft_execute_cheapest_move(td_list **stack_a, td_list **stack_b);

/*stack_util_b***************************************************/
int			ft_find_insert_position(td_list *stack_a, int value);
int			ft_find_cheapest_index(td_list *stack_b);

#endif