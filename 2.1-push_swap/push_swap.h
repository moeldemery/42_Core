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

# define DEBUG 1

void ft_list_print(td_list *lst);
int ft_is_str_digit(char *str);
/*****************************************************/
void	ft_stack_swap(td_list **stack);
void	ft_stack_push(td_list **src, td_list **dest);
void	ft_stack_rotate(td_list **stack);
void	ft_stack_reverse_rotate(td_list **stack);
/*****************************************************/
void	ft_sa(td_list **stack_a);
void	ft_pa(td_list **stack_a, td_list **stack_b);
void	ft_ra(td_list **stack_a);
void	ft_rra(td_list **stack_a);
/*****************************************************/
void	ft_sb(td_list **stack_b);
void	ft_pb(td_list **stack_a, td_list **stack_b);
void	ft_rb(td_list **stack_b);
void	ft_rrb(td_list **stack_b);
/*****************************************************/
void	ft_ss(td_list **stack_a, td_list **stack_b);
void	ft_rr(td_list **stack_a, td_list **stack_b);
void	ft_rrr(td_list **stack_a, td_list **stack_b);
/*****************************************************/
void	ft_sort_stack(td_list **stack_a, td_list **stack_b);
void	ft_sort_three(td_list **stack);
void	ft_sort_four(td_list **stack_a, td_list **stack_b);
void	ft_sort_five(td_list **stack_a, td_list **stack_b);
void    ft_sort_n(td_list **stack_a, td_list **stack_b,  int size);
/****************************************************/
int		ft_is_sorted(td_list *stack);
int		ft_find_min(td_list *stack);
int		ft_find_max(td_list *stack);
/****************************************************/

void ft_debug_print_lis(int *lis, int size);


void ft_init_array_lis( int *lis, int size, int value);
int	*ft_find_lis(td_list **stack_a, int size);
void ft_set_max_lis_mask(td_list *stack_a, int *lis_cost, int **lis_mask, int size, int max_len);
void ft_print_cost_lis(int **cost_lis, int size);
int ft_calculate_lis(td_list *stack_a, int size);
void    ft_push_non_lis(td_list **stack_a, td_list **stack_b, int *lis, int size);


/****************************************************/

#endif