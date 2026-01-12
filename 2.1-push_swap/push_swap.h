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

void ft_list_print(t_list *lst);
int ft_is_str_digit(char *str);
/*****************************************************/
void	ft_stack_swap(t_list **stack);
void	ft_stack_push(t_list **src, t_list **dest);
void	ft_stack_rotate(t_list **stack);
void	ft_stack_reverse_rotate(t_list **stack);
/*****************************************************/
void	ft_sa(t_list **stack_a);
void	ft_pa(t_list **stack_a, t_list **stack_b);
void	ft_ra(t_list **stack_a);
void	ft_rra(t_list **stack_a);
/*****************************************************/
void	ft_sb(t_list **stack_b);
void	ft_pb(t_list **stack_a, t_list **stack_b);
void	ft_rb(t_list **stack_b);
void	ft_rrb(t_list **stack_b);
/*****************************************************/
void	ft_ss(t_list **stack_a, t_list **stack_b);
void	ft_rr(t_list **stack_a, t_list **stack_b);
void	ft_rrr(t_list **stack_a, t_list **stack_b);
/*****************************************************/
void	ft_sort_stack(t_list **stack_a, t_list **stack_b);
void	ft_sort_three(t_list **stack);
void	ft_sort_four(t_list **stack_a, t_list **stack_b);
void	ft_sort_five(t_list **stack_a, t_list **stack_b);
void    ft_sort_n(t_list **stack_a, t_list **stack_b,  int size);
/****************************************************/
int		ft_is_sorted(t_list *stack);
int		ft_find_min(t_list *stack);
int		ft_find_max(t_list *stack);
/****************************************************/

void ft_init_array_lis(t_list **stack_a, int *lis, int size);
int	*ft_find_lis(t_list **stack_a, int size);
void    ft_set_max_lis(t_list *stack_a, int **dp, int max_index);
int ft_calculate_lis(t_list *stack_a, int **arr, int **dp, int size);
void    ft_push_non_lis(t_list **stack_a, t_list **stack_b, int *lis, int size);


/****************************************************/

#endif